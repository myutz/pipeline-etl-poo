# Módulo 1 — Leitura de CSV com Python puro
# Lê o arquivo pecas_produzidas.csv e estrutura os dados

import csv
import os
from datetime import datetime

pasta_atual = os.path.dirname(__file__)
caminho_csv = os.path.join(pasta_atual, 'pecas_produzidas.csv')

if __name__ == '__main__':
    with open(caminho_csv, 'r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        pecas = []
        for linha in leitor:
            peca = {
                'id': int(linha['id']),
                'divindade': linha['divindade'],
                'complexidade': linha['complexidade'].lower(),
                'tempo_cura_minutos': linha['tempo_cura_minutos'],
                'peso_gramas': float(linha['peso_gramas']),
                'preco_venda': float(linha['preco_venda']),
                'data_producao': datetime.strptime(linha['data_producao'], '%d/%m/%Y').date()
            }
            pecas.append(peca)

        print(f'Total de peças lidas: {len(pecas)}')