import pandas as pd
import os

pasta_atual = os.path.dirname(__file__)
caminho_csv = os.path.join(pasta_atual, 'pecas_produzidas.csv')

df = pd.read_csv(caminho_csv)

print(df)
print(df.dtypes)   # mostra o tipo de cada coluna
print('--------------------------------')
print(df.shape)    # mostra quantas linhas e colunas tem
print('--------------------------------')


# # QUANTIDADE POR DIVINDADE:
# print(df['divindade'].value_counts())
# print('--------------------------------')

# # PREÇO MÉDIO:
# print(df['preco_venda'].mean())
# print('--------------------------------')

# # CONTAGEM POR COMPLEXIDADE:
# print(df['complexidade'].value_counts())
# print('--------------------------------')

# # SÓ AS PEÇAS DE GANESHA
# print(df['divindade'] == 'Ganesha')
# print(df[df['divindade'] == 'Ganesha'])

# PEÇAS COM PREÇO A PARTIR DE $20:
# print(df[df['preco_venda'] > 20])

# PEÇAS SIMPLES
# print(df[df['complexidade'] == 'Simples'])

# # DOIS FILTRO AO MESMO TEMPO
# print(df[(df['divindade'] == 'Ganesha') & (df['preco_venda'] > 20)])

# filtro = df[df['preco_venda'] > 20]
# print(filtro.shape)  # quantas linhas passaram pelo filtro?

# FILTRO - NÂO:
# print(df[~(df['complexidade'] == 'Simples')])

print(df.groupby('divindade')['preco_venda'].sum().sort_values(ascending=False))

# 1. Faz o agrupamento, soma, ordena e transforma de volta em uma tabela (DataFrame)
df_relatorio = df.groupby('divindade')['preco_venda'].sum().sort_values(ascending=False).reset_index()

# 2. Renomeia as colunas para o relatório ficar profissional
df_relatorio.columns = ['Divindade', 'Faturamento_Total']

# 3. Define onde salvar (na mesma pasta do seu projeto)
caminho_saida = os.path.join(pasta_atual, 'faturamento_por_divindade.csv')

# 4. O "LOAD": Salva o arquivo final! (index=False serve para não criar uma coluna de números inúteis)
df_relatorio.to_csv(caminho_saida, index=False)

print("Pipeline executado com sucesso! Procure pelo arquivo 'faturamento_por_divindade.csv' na sua pasta.")