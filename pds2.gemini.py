import pandas as pd
import os

pasta_atual = os.path.dirname(__file__)
caminho_csv = os.path.join(pasta_atual, 'pecas_produzidas.csv')

df = pd.read_csv(caminho_csv)

# ==========================================
# PARTE 1: Transformar minutos em horas
# ==========================================
# Crie uma coluna nova chamada 'tempo_cura_horas' dividindo a coluna 'tempo_cura_minutos' por 60
# SEU CÓDIGO AQUI
df['tempo_cura_horas'] = df['tempo_cura_minutos'] / 60

# ==========================================
# PARTE 2: Corrigir o tipo da data
# ==========================================
# Sobrescreva a coluna 'data_producao' usando o pd.to_datetime para que ela vire data de verdade
# SEU CÓDIGO AQUI
df['data_producao'] = pd.to_datetime(df['data_producao'], format='%d/%m/%Y')


# ==========================================
# TESTE DO ENGENHEIRO (Se funcionar, isso aqui roda sem erro)
# ==========================================
print("--- TIPOS DE DADOS ATUALIZADOS ---")
print(df.dtypes) 
# Esperado: 'data_producao' agora deve ser datetime64, e 'tempo_cura_horas' deve aparecer na lista.

print("\n--- VISUALIZAÇÃO DA NOVA COLUNA ---")
print(df[['divindade', 'tempo_cura_minutos', 'tempo_cura_horas']].head())

# TESTE DE ENGENHARIA DE DADOS: Filtrar por data real
# Agora que é data de verdade, podemos usar operadores como "maior que" (>)
print("\n--- PEÇAS PRODUZIDAS A PARTIR DE JUNHO DE 2024 ---")
print(df[df['data_producao'] > '2024-06-01'].sort_values(by='data_producao', ascending=True))

# Qual divindade deu mais dinheiro (faturamento) para a empresa nesse período depois de junho de 2024?
# MINHA RESOLUÇÃO:
# print((df[df['data_producao'] > '2024-06-01'].sort_values(by='data_producao', ascending=False))) & (df.groupby('divindade')['preco_venda'].sum())
print('-----------------------------------------------------------------------------------------------------------------------------')

# RESOLUÇÃO CORRETA:
# Tudo junto em uma única linha de comando:
relatorio_final = df[df['data_producao'] > '2024-06-01'].groupby('divindade')['preco_venda'].sum().sort_values(ascending=False)

print(relatorio_final)

# Crie uma linha de código que agrupe os dados pela coluna de complexidade, some o preço de venda e ordene do maior faturamento para o menor:
print(df.groupby('complexidade')['preco_venda'].sum().sort_values(ascending=False))


# Escreva o comando que filtra as peças produzidas a partir de 1º de julho de 2024, selecione a coluna peso_gramas e faça a soma total.
print(df[df['data_producao'] > '2024-07-01'].groupby('divindade')['peso_gramas'].sum() / 1000)

# Agrupe os dados por divindade, calcule a média (.mean()) da coluna nova que você criou (tempo_cura_horas) e ordene o resultado do maior tempo para o menor.
print(df.groupby('divindade')['tempo_cura_horas'].mean().sort_values(ascending=False))

print(df['peso_gramas'])
print(df[['divindade', 'peso_gramas', 'data_producao']])
