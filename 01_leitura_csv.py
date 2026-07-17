import csv
import os
from datetime import datetime

pasta_atual = os.path.dirname(__file__)
caminho_csv = os.path.join(pasta_atual, 'pecas_produzidas.csv')


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
    print(pecas)
    
    
    contagem = {}
    preco_total = 0
    pecas_simples = 0
    pecas_detalhes = 0
    for peca in pecas:
        nome = peca['divindade']
        preco_total += peca['preco_venda']
        if nome in contagem:
            contagem[nome] += 1
        else:
            contagem[nome] = 1
        if peca['complexidade'] == 'simples':
            pecas_simples += 1
        elif peca['complexidade'] == 'com detalhes':
            pecas_detalhes += 1
    print(f'Quantidade de peças = {contagem}')
    print(f'Valor médio = {preco_total / len(pecas):.2f}')
    print(f'Temos {pecas_simples} peças simples e {pecas_detalhes} peças com detalhes.')
    


