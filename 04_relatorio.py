import pandas as pd
import os

pasta_atual = os.path.dirname(__file__)
caminho_csv = os.path.join(pasta_atual, 'pecas_produzidas.csv')

df = pd.read_csv(caminho_csv)
print(df.head())

# 1:
print(df.groupby('divindade')['preco_venda'].sum().sort_values(ascending=False))


# 2:
df['preco_por_grama'] = df['preco_venda'] / df['peso_gramas']
print(df.groupby(['complexidade'])['preco_por_grama'].mean().sort_values(ascending=False))


# 3:
df['data_producao'] = pd.to_datetime(df['data_producao'], format='%d/%m/%Y')
df['trimestre'] = df['data_producao'].dt.quarter
print(df.groupby('trimestre')['id'].count())


# 4:
print(df.groupby('divindade')['preco_por_grama'].mean().sort_values(ascending=True))

# Pergunta 1
# Qual o peso total de resina usado por divindade? Ordena do maior pro menor.
print(df.groupby('divindade')['peso_gramas'].sum().sort_values(ascending=False))
print('---------------------------------------------------------------------------')

# Pergunta 2
# Qual a média de preço de venda das peças simples produzidas no 2º trimestre?
# (essa combina filtro + agrupamento)
filtro = (df['complexidade'] == 'Simples') & (df['trimestre'] == 2)
print(df[filtro]['preco_venda'].mean())


# Pergunta 3
# Quais divindades tiveram mais de 7 peças produzidas no ano?
contagem = df.groupby('divindade')['id'].count()
print(contagem[contagem >= 7])


# Pergunta 4
# Qual o mês com maior receita total?
df['mes'] = df['data_producao'].dt.month_name()
print(df.groupby('mes')['preco_venda'].sum().sort_values(ascending=False))

# 🔧 Rodada 3 — Raciocínio puro
# Pergunta 1
# Qual a receita média por trimestre?
print(df.groupby('trimestre')['preco_venda'].mean())
print(df.head())

# Pergunta 2
# Quais peças têm preco_por_grama acima da média geral?
media_geral = df['preco_por_grama'].mean()
filtro = df[df['preco_por_grama'] > media_geral]
print(filtro.shape[0])

# Pergunta 3
# Qual divindade teve maior peso total de resina usada no 2º semestre?
segundo_semestre = df['trimestre'] > 2
print(df[segundo_semestre].groupby('divindade')['peso_gramas'].sum().sort_values(ascending=False))


# Pergunta 4
# Quantas peças de cada complexidade foram produzidas por trimestre?
print(df.head())
quantidade = df.groupby(['complexidade', 'trimestre'])['id'].count()
print(quantidade)

# 🔧 Rodada 4 — Módulo 4
# Pergunta 1
# Qual o peso médio das peças produzidas no 1º trimestre, separado por divindade?
filtro = df['trimestre'] == 1
peso = df[filtro].groupby(['divindade'])['peso_gramas'].mean()
print(peso)

# Pergunta 2
# Quais divindades tiveram receita total acima de R$ 100 no ano?
filtro = df.groupby('divindade')['preco_venda'].sum()
print(filtro[filtro > 100])
