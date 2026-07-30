import sqlite3
import os

pasta_atual = os.path.dirname(__file__)
caminho_banco = os.path.join(pasta_atual, 'sql_avancado.db')

conn = sqlite3.connect(caminho_banco)
cursor = conn.cursor()

# Tabela de moldes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS moldes (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        tipo_borracha TEXT,
        usos_maximos INTEGER
    )
''')

# Tabela de peças — com referência ao molde
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pecas (
        id INTEGER PRIMARY KEY,
        divindade TEXT,
        complexidade TEXT,
        preco_venda REAL,
        molde_id INTEGER,
        FOREIGN KEY (molde_id) REFERENCES moldes(id)
    )
''')

conn.commit()
print('Tabelas criadas!')

# Inserindo moldes
cursor.executemany('''
    INSERT OR IGNORE INTO moldes (id, nome, tipo_borracha, usos_maximos)
    VALUES (?, ?, ?, ?)
''', [
    (1, 'Ganesha', 'Silicone', 50),
    (2, 'Lakshmi', 'Silicone', 100),
    (3, 'Buda', 'PU', 80),
    (4, 'Shiva', 'Silicone', 60),
])

# Inserindo peças
cursor.executemany('''
    INSERT OR IGNORE INTO pecas (id, divindade, complexidade, preco_venda, molde_id)
    VALUES (?, ?, ?, ?, ?)
''', [
    (1, 'Ganesha', 'Com Detalhes', 25.68, 1),
    (2, 'Lakshmi', 'Com Detalhes', 21.72, 2),
    (3, 'Buda', 'Simples', 30.50, 3),
    (4, 'Shiva', 'Com Detalhes', 28.00, 4),
    (5, 'Ganesha', 'Com Detalhes', 24.50, 1),
    (6, 'Buda', 'Simples', 31.00, 3),
    (7, 'Krishna', 'Simples', 12.50, None),  # sem molde cadastrado!
])

conn.commit()
print('Dados inseridos!')

cursor.execute('''
    SELECT pecas.divindade, pecas.preco_venda, moldes.nome, moldes.tipo_borracha
    FROM pecas
    LEFT JOIN moldes ON pecas.molde_id = moldes.id
''')

resultados = cursor.fetchall()
print('=== INNER JOIN ===')
for row in resultados:
    print(row)

# Qual o preço médio de venda por tipo de borracha do molde?
cursor.execute('''
    SELECT tipo_borracha, AVG(preco_venda)
    FROM moldes
    INNER JOIN pecas ON pecas.molde_id= moldes.id
    GROUP BY tipo_borracha
''')

resultado = cursor.fetchall()
print(' **** PREÇO MÉDIO POR BORRACHA ****')
print(resultado)
