# Módulo 6 - Pipeline ETL
# Utilizando POO, extrai os dados do  nosso arquivo CSV original, transforma alguns dados em novas colunas, e carrega um novo arquivo SQL.
import pandas as pd
import sqlite3
import os

class Extrator:
    def __init__(self, caminho_csv):
        self.caminho_csv = caminho_csv

    def extrair(self):
        df = pd.read_csv(self.caminho_csv)
        print(f'Extrator: {len(df)} registros carregados.')
        return df

class Transformador:
    def __init__(self, df):
        self.df = df
    
    def transformar(self):
        df = self.df.copy()
        df['data_producao'] = pd.to_datetime(df['data_producao'], format='%d/%m/%Y')
        df['tempo_cura_horas'] = df['tempo_cura_minutos'] / 60
        df['preco_por_grama'] = df['preco_venda'] / df['peso_gramas']
        df['trimestre'] = df['data_producao'].dt.quarter
        print(f'Transformador: {len(df.columns)} colunas após transformação.')
        return df

class Carregador:
    def __init__(self, caminho_banco):
        self.caminho_banco = caminho_banco

    def carregar(self, df):
        conn = sqlite3.connect(self.caminho_banco)
        df.to_sql('pecas', conn, if_exists='replace', index=False)
        print(f'Carregador: {len(df)} registros salvos no banco.')
        conn.close()


if __name__ == '__main__':
    pasta_atual = os.path.dirname(__file__)
    caminho_csv = os.path.join(pasta_atual, 'pecas_produzidas.csv')
    caminho_banco = os.path.join(pasta_atual, 'producao_etl.db')

    # E (Extract)
    extrator = Extrator(caminho_csv)
    df_bruto = extrator.extrair()

    # T (Transform)
    transformador = Transformador(df_bruto)
    df_transformado = transformador.transformar()
    
    # L (Load)
    carregador = Carregador(caminho_banco)
    carregador.carregar(df_transformado)

    print('Pipeline ETL concluído!')