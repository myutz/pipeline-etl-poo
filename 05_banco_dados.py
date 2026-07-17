import sqlite3
import pandas as pd
import os

pasta_atual = os.path.dirname(__file__)
caminho_banco = os.path.join(pasta_atual, 'producao.db')
caminho_csv = os.path.join(pasta_atual, 'pecas_produzidas.csv')  # ← adiciona essa linha

# Cria a conexão — se o arquivo não existir, o SQLite cria automaticamente
conn = sqlite3.connect(caminho_banco)
cursor = conn.cursor()

print('Banco conectado!')

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

conn.commit()  # confirma a operação no banco
print('Tabela criada!')

df = pd.read_csv(caminho_csv)

df.to_sql('pecas', conn, if_exists='replace', index=False)

print(f'{len(df)} registros inseridos!')

cursor.execute('SELECT * FROM pecas LIMIT 5')
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

# ---------------------------------------------------------------------------------------------

cursor.execute('''
    SELECT divindade, SUM(preco_venda) as receita_total
    FROM pecas
    GROUP BY divindade
    ORDER BY receita_total DESC
''')

resultados = cursor.fetchall()
for divindade, receita in resultados:
    print(f'{divindade}: R$ {receita:.2f}')


#  Consulta 1 - Quantas peças foram produzidas por complexidade?
cursor.execute('''
    SELECT complexidade, COUNT(id)
    FROM pecas
    GROUP BY complexidade
               ''')

resultados = cursor.fetchall()
for divindade in resultados:
    print(divindade)
print('------------------------------------------------------------------------------------------')
# Consulta 2 - Qual o peso médio por divindade, ordenado do maior pro menor?
cursor.execute('''
    SELECT divindade, AVG(peso_gramas) as media_peso
    FROM pecas
    GROUP BY divindade
    ORDER BY  media_peso DESC
               ''')
resultados = cursor.fetchall()
for divindade, media in resultados:
    print(f'{divindade} - Peso médio: {media:.2f}')

conn.close()
print('Conexão encerrada.')