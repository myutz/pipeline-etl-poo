# Módulo 3 - Tratando tipo de dados.
# Transformando dados em novas colunas de informações.
import pandas as pd
import os

pasta_atual = os.path.dirname(__file__)
caminho_csv = os.path.join(pasta_atual, 'pecas_produzidas.csv')

df = pd.read_csv(caminho_csv)


if __name__ == '__main__':
    # TRANSFORMANDO COLUNA MINUTOS EM HORAS:
    df['tempo_cura_horas'] = df['tempo_cura_minutos'] / 60
    print(df[['divindade', 'tempo_cura_minutos', 'tempo_cura_horas']].head())

    # CRIANDO NOVA COLUNA preco_por_grama A PARTIR DE OUTRAS 2:
    df['preco_por_grama'] = df['preco_venda'] / df['peso_gramas']
    print(df[['divindade', 'preco_venda', 'peso_gramas', 'preco_por_grama']].head())

    # CONVERTENDO data_producao DE STRING PARA DATE:
    df['data_producao'] = pd.to_datetime(df['data_producao'], format='%d/%m/%Y')
    print(f'Tipo de data_producao: {df["data_producao"].dtype}')

    # CLASSIFICANDO PEÇAS A PARTIR DO PESO:
    df['categoria_peso'] = pd.cut(
        df['peso_gramas'],
        bins=[0, 500, 1000, 2000],
        labels=['Leve', 'Médio', 'Pesado']
    )

    print(df['categoria_peso'].value_counts())

