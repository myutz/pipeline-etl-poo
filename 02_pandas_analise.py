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

# print(df.groupby('divindade')['preco_venda'].sum().sort_values(ascending=False))

# 1. Qual o peso médio (em gramas) das peças por complexidade (Simples vs Com Detalhes)?
# peso_medio = df.groupby(['divindade', 'complexidade'])['peso_gramas'].mean()
# print(peso_medio)

# 2. Filtre apenas as peças produzidas com peso acima de 1000g e me diz quantas são.
# print(df[df['peso_gramas'] >= 1000].shape)

# 3. Qual divindade tem o menor preço médio de venda? (dica: mean() + sort_values())
# print(df.groupby('divindade')['preco_venda'].mean().sort_values(ascending=True))

# 4. Quantas peças foram produzidas por mês? (dica: data_producao tem um atributo .dt.month que extrai o mês — mas pra isso funcionar, a coluna precisa estar no tipo datetime, não string)
df['data_producao'] = pd.to_datetime(df['data_producao'], format='%d/%m/%Y')
print(df.groupby(df['data_producao'].dt.month_name())['id'].count())

print(df.loc[5])