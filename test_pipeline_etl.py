from pipeline_etl import Extrator, Transformador, Carregador
import pytest
import os
import pandas as pd
import sqlite3


def test_extrair():
    pasta_atual = os.path.dirname(__file__)
    caminho_csv = os.path.join(pasta_atual, 'pecas_produzidas.csv')
    
    extrator = Extrator(caminho_csv)
    df = extrator.extrair()
    assert df.shape[0]

def test_extrair_arquivo_inexistente():
    with pytest.raises(FileNotFoundError):
        pasta_atual = os.path.dirname(__file__)
        caminho_csv = os.path.join(pasta_atual, 'arquivo_falso.csv')
        
        extrator = Extrator(caminho_csv)
        df = extrator.extrair()

def test_transformar_data_producao():
    df = pd.DataFrame({"data_producao": ["16/08/2026"], 
                       "tempo_cura_minutos": [60],
                        "preco_venda": [500],
                        "peso_gramas": [20]})
    transformador = Transformador(df)
    df = transformador.transformar()
    assert df.dtypes["data_producao"] == "datetime64[us]"

def test_transformar_coluna_ausente():
    with pytest.raises(KeyError):
        df = pd.DataFrame({"data_producao": ["16/08/2026"], 
                       "tempo_cura_minutos": [60],
                        "peso_gramas": [20]})
        transformador = Transformador(df)
        df = transformador.transformar()

def test_carregar_caminho_errado():
    df = pd.read_csv("pecas_produzidas.csv")
    with pytest.raises(sqlite3.OperationalError):
        carregador = Carregador('C:/pasta_falsa/banco.db')
        df = carregador.carregar(df)

def test_carregar_caminho_feliz(tmp_path):
    caminho_banco = tmp_path / "teste.db"
    df = pd.DataFrame({"data_producao": ["16/08/2026"],
                       "tempo_cura_minutos": [60],
                       "peso_gramas": [20]})
    carregador = Carregador(caminho_banco)
    carregar = carregador.carregar(df)
    conn = sqlite3.connect(caminho_banco) 
    df_salvo = pd.read_sql('SELECT * FROM pecas', conn)
    assert df.shape[0] == df_salvo.shape[0]


        
    
