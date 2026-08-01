# Módulo 2 — Análise exploratória com Pandas
# Primeira análise dos dados: estrutura, quantidade, médias e contagens

import pandas as pd
import os

pasta_atual = os.path.dirname(__file__)
caminho_csv = os.path.join(pasta_atual, 'pecas_produzidas.csv')

df = pd.read_csv(caminho_csv)

if __name__ == '__main__':
    print(df.dtypes)   # mostra o tipo de cada coluna
    print(df.shape)    # mostra quantas linhas e colunas tem

    # QUANTIDADE DE DADOS FALTANTES:
    dados_faltantes = df.isnull().sum()
    print(dados_faltantes)
    
    # QUANTIDADE POR DIVINDADE:
    quantidade = df['divindade'].value_counts()
    print(f'Quantidade de divindades:\n{quantidade}')
    
    # PREÇO MÉDIO:
    preco_medio = df['preco_venda'].mean()
    print(f'Preço médio do nosso DF:\n{preco_medio:.2f}')
    
    # CONTAGEM POR COMPLEXIDADE:
    qtd_complexidade = df['complexidade'].value_counts()
    print(f'Quantidade de produtos por complexidade:\n{qtd_complexidade}')
    