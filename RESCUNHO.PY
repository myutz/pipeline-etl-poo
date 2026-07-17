import pandas as pd
import os

pasta_atual = os.path.dirname(__file__)
caminho_csv = os.path.join(pasta_atual, 'pecas_produzidas.csv')

df = pd.read_csv(caminho_csv)
print(df.head())
print(df.info())
# print(df(df['divindade'] == 'Ganesha').mean['peso_gramas'])
print(df[df['divindade'] == 'Ganesha']['peso_gramas'].mean())

print(f'Peso das médio {df.groupby('divindade')['peso_gramas'].mean().sort_values(ascending=False)}')