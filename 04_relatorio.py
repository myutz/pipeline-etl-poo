# Módulo 4 - Gerando relatórios
# Novos relatórios gerados a partir de informações já existentes no arquivo CSV.
import pandas as pd
import os

pasta_atual = os.path.dirname(__file__)
caminho_csv = os.path.join(pasta_atual, 'pecas_produzidas.csv')

df = pd.read_csv(caminho_csv)

if __name__ == '__main__':
    # TOP PRODUTOS MAIS VENDIDOS:
    top_produtos = df.groupby('divindade')['preco_venda'].sum().sort_values(ascending=False)
    print(f'Produtos mais vendidos: \n {top_produtos}')

    # PREÇO DE CADA GRAMA:
    df['preco_por_grama'] = df['preco_venda'] / df['peso_gramas']
    print(f'Preço por grama em cada produto: \n {df['preco_por_grama'].head()}')

    # MÉDIA POR complexidade:
    media_complexidade = df.groupby(['complexidade'])['preco_por_grama'].mean().sort_values(ascending=False)
    print(media_complexidade)

    # QUANTIDADE DE VENDAS POR TRIMESTRE:
    df['data_producao'] = pd.to_datetime(df['data_producao'], format='%d/%m/%Y')
    df['trimestre'] = df['data_producao'].dt.quarter
    print(df.groupby('trimestre')['id'].count())

    # MÉDIA preco_por_grama POR DIVINDADE:
    media_divindade = df.groupby('divindade')['preco_por_grama'].mean().sort_values(ascending=True)
    print(media_divindade)

    
    # QUANTIDADE TOTAL DE MATERIAL GASTO POR DIVINDADE:
    quantidade_materia_divindade = df.groupby('divindade')['peso_gramas'].sum().sort_values(ascending=False)
    print(quantidade_materia_divindade)
    
    # DIVINDADES QUE TIVERAM MAIS DE 7 PEÇAS PRODUZIDAS NO ANO:
    contagem = df.groupby('divindade')['id'].count()
    print(contagem[contagem >= 7])

    # MÊS COM MAIOR RECEITA:
    df['mes'] = df['data_producao'].dt.month_name()
    mes_maior_receita = df.groupby('mes')['preco_venda'].sum().sort_values(ascending=False)
    print(mes_maior_receita)

    # RECEITA MÉDIA POR TRIMESTRE:
    media_trimestre = df.groupby('trimestre')['preco_venda'].mean()
    print(media_trimestre)

    # PRODUTOS COM preco_por_grama ACIMA DA MÉDIA GERAL:
    media_geral = df['preco_por_grama'].mean()
    filtro = df[df['preco_por_grama'] > media_geral]
    print(filtro)

    # DIVINDADE QUE TEVE MAIOR PESO TOTAL DE RESINA USADA NO 2º SEMESTRE:
    segundo_semestre = df['trimestre'] > 2
    print(df[segundo_semestre].groupby('divindade')['peso_gramas'].sum().sort_values(ascending=False))


    # QUANTIDADE DE PEÇAS DE CADA COMPLEXIDADE PRODUZIDAS POR TRIMESTRE:
    quantidade = df.groupby(['complexidade', 'trimestre'])['id'].count()
    print(quantidade)

    # DIVINDADES QUE TIVERAM RECEITA TOTAL ACIMA DE R$100 NO ANO:
    filtro = df.groupby('divindade')['preco_venda'].sum()
    print(filtro[filtro > 100])