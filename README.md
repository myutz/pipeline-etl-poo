
# PIPELINE ETL

## O problema:
Pipeline ETL que processa dados reais de produção de peças de resina do ano de 2024.
Depois de importar, tratar e carregar os dados no banco, as consultas SQL respondem perguntas de negócio:

- Faturamento por peça
- Quantidade de peças por complexidade
- Preço médio de cada peça
- Quais tipos de borracha são usados e quanto representam em R$

Com esses resultados é possível analisar se alguma peça precisa de reajuste e qual silicone compensa mais.

## Ferramentas utilizadas:

- Python 3.12 : Aplicando orientação a objetos (Extrator, Transformador, Carregador) 
- Pandas : Leitura do CSV e transformação dos dados 
- SQLite : Armazenamento e consulta de dados 
- PyTest: 6 testes que verificam erros nas classes Extrator, Transformador, Carregador, pensamos em alguns problemas que poderiam dar errado antes que aconteça. 
- Git: Para versionamento do código.  Trabalhamos com branches separadas para cada etapa do processo, depois que obtivemos nossas condições ideais fizemos um pull request e o merge na main.

## Como rodar:

```bash
git clone <url>
cd "Eng Dados"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python pipeline_etl.py
```

## Saída esperada:

```
Extrator: 60 registros carregados.
Transformador: 10 colunas após transformação.
Carregador: 60 registros salvos no banco.
Pipeline ETL concluído!
```

### Evolução didática (01 a 04):

Arquivos de evolução didática, passo a passo para o aprendizado sobre um .csv.

- 01_leitura_csv.py: leitura dos dados do CSV
- 02_pandas_analise.py: trabalhando com pandas para consultas e análises sobre os dados
- 03_transformacao.py: novas colunas a partir de outras já existentes e tratamento de tipos de dados
- 04_relatorio.py: análises com regras de negócio

### Consultas de negócio (05_banco_dados.py):

Aqui construímos um banco de dados localmente com sqlite3 para salvar dados vindos do .csv e criamos uma nova tabela 'moldes' para responder perguntas baseadas em regra de negócio.

### Pipeline final (pipeline_etl.py):

Extrai, transforma e carrega nossos dados em um .db. Aplicando POO, cada classe tem sua responsabilidade e com isso cada uma é testável.

## Comando para rodar os testes: 

`pytest test_pipeline_etl.py`

Cobrimos 6 testes;
* `test_extrair`: Garantimos que a extração será correta do arquivo .csv
* `test_extrair_arquivo_inexistente`: Caso não exista o arquivo que passamos para a extração
* `test_transformar_data_producao`: Garantimos que tratamos o corretamente o tipo de dado da coluna "data_producao" em datetime[us].
* `test_transformar_coluna_ausente`: passamos um DataFrame sem a coluna `preco_venda` de propósito, garantindo que o `Transformador` levanta `KeyError` quando falta uma coluna necessária.
* `test_carregar_caminho_errado`: Se nosso sqlite não conseguir carregar corretamente o caminho da pasta.
* `test_carregar_caminho_feliz`: Carregamos o caminho correto no sqlite3 verificamos se os dados foram carregados corretamente.

## Por que 2 .db separados?

producao.db vem de origem do arquivo 05_banco_dados.py, vem de outro contexto de aprendizagem. E producao_etl.db é gerado pelo nosso arquivo pipeline_etl.py que trabalhamos com POO.
Futuramente pretendo unificar esses processos em 1 só, gerando apenas 1 .db para que as consultas nos arquivos 04 e 05 sejam feitas em cima do .db que o arquivo pipeline_etl.py gerou.

## Melhorias futuras:

Ainda no meu plano de estudo sobre esse projeto, pretendo aplicar meu conhecimento com Docker e PostgreSQL para evoluir o projeto / meus conhecimentos.

## Contexto do projeto:

Esse projeto foi construído baseado no meu trabalho atual, utilizando processos e conhecimentos que tenho sobre ele, utilizei isso com oque estou aprendendo no meu curso de Sistema de informação e cursos por fora, como python, pandas, SQL e outras ferramentas pra trabalhar com dados.