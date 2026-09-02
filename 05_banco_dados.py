# Módulo 5 - Banco de Dados
# Utilizando sqlite3 para criar nossas tabelas. Fazendo algumas consultas com SQL para validação.
import sqlite3
import pandas as pd
import os

pasta_atual = os.path.dirname(__file__)
caminho_banco = os.path.join(pasta_atual, 'producao.db')
caminho_csv = os.path.join(pasta_atual, 'pecas_produzidas.csv')  # ← adiciona essa linha


if __name__ == '__main__':
    # Cria a conexão — se o arquivo não existir, o SQLite cria automaticamente
    conn = sqlite3.connect(caminho_banco)
    cursor = conn.cursor()
    print('Banco conectado!')

    cursor.execute('DROP TABLE IF EXISTS pecas')   # primeiro as filhas
    cursor.execute('DROP TABLE IF EXISTS moldes')  # depois a pai
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pecas (
            id INTEGER PRIMARY KEY,
            divindade TEXT,
            complexidade TEXT,
            tempo_cura_minutos INTEGER,
            peso_gramas REAL,
            preco_venda REAL,
            data_producao TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS moldes (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            tipo_borracha TEXT,
            peso INTEGER,
            data_fabricacao TEXT,
            uso_maximo INTEGER
        )
    ''')

    moldes = [
    (1, 'Ganesha',   'Silicone', 1200, '01/01/2023', 100),
    (2, 'Lakshmi',   'Silicone',  800, '15/03/2023', 80),
    (3, 'Buda',      'PU',       1800, '10/06/2022', 150),
    (4, 'Shiva',     'Silicone', 1500, '20/01/2023', 80),
    (5, 'Durga',     'PU',       1000, '05/09/2022', 50),
    (6, 'Hanuman',   'Silicone',  600, '11/11/2023', 70),
    (7, 'Krishna',   'Silicone',  300, '30/04/2023', 50),
    (8, 'Saraswati', 'PU',        400, '17/07/2022', 50),
]

    cursor.executemany('''
        INSERT OR IGNORE INTO moldes (id, nome, tipo_borracha, peso, data_fabricacao, uso_maximo)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', moldes)

    # CONFIRMA A CRIAÇÃO DA TABELA NO BANCO DE DADOS:
    conn.commit()
    print('Tabela criada!')

    df_moldes = pd.DataFrame(moldes, columns=['id', 'nome', 'tipo_borracha', 'peso', 'data_fabricacao', 'uso_maximo'])
    df = pd.read_csv(caminho_csv)

    df = df.merge(
        df_moldes[['id', 'nome']],
        left_on='divindade',
        right_on='nome'
    )
    df = df.rename(columns={'id_y': 'molde_id', 'id_x': 'id'})
    print(df.head())

    
    df.to_sql('pecas', conn, if_exists='replace', index=False)
    print(f'{len(df)} registros inseridos!')

    # CONSULTA NOSSOS PRIMEIROS 5 DADOS DA NOSSA TABELA:
    cursor.execute('SELECT * FROM pecas LIMIT 5')
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)

    # RECEITA TOTAL POR PRODUTO:
    cursor.execute('''
        SELECT divindade, SUM(preco_venda) as receita_total
        FROM pecas
        GROUP BY divindade
        ORDER BY receita_total DESC
    ''')

    resultados = cursor.fetchall()
    for divindade, receita in resultados:
        print(f'{divindade}: R$ {receita:.2f}')

    # QUANTIDADE DE PEÇAS POR COMPLEXIDADE:
    cursor.execute('''
        SELECT complexidade, COUNT(id)
        FROM pecas
        GROUP BY complexidade
                ''')
    
    resultados = cursor.fetchall()
    print('Complexidade e quantidade de peças:')
    for complexidade, quantidade in resultados:
        print(f'{complexidade} = {quantidade}')

    # PESO MÉDIO DAS DINVINDADES, ORDENANDO DO MENOR PARA O MAIOR:
    cursor.execute('''
        SELECT divindade, AVG(peso_gramas) as media_peso
        FROM pecas
        GROUP BY divindade
        ORDER BY  media_peso ASC
                ''')
    resultados = cursor.fetchall()
    for divindade, media in resultados:
        print(f'{divindade} - Peso médio: {media:.2f}')

    cursor.execute('''
        SELECT tipo_borracha, SUM(preco_venda) as valor_total
        FROM moldes
        JOIN pecas ON pecas.molde_id = moldes.id
        GROUP BY tipo_borracha
        ORDER BY valor_total DESC
        ''')
    resultados = cursor.fetchall()
    for tipo_borracha, valor_total in resultados:
        print(f'{tipo_borracha}: R$ {valor_total:.2f}')

    conn.close()
    print('Conexão encerrada.')

    