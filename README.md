# Projeto ETL: Extração de Dados de uma API

## Visão Geral do Projeto

 Este projeto implementa um pipeline ETL (Extract, Transform, Load) para extrair dados de uma API externa, processá-los de acordo com os requisitos de negócio e armazenar os dados transformados em um banco de dados para análise posterior.

## Principais Características

Extração: Os dados são buscados de uma API externa usando requisições HTTP RESTful.

Transformação: Os dados são limpos, normalizados e estruturados para atender aos requisitos de negócio.

Carregamento: Os dados processados são armazenados em um banco de dados relacional para consultas e análises eficientes.

## Requisitos Prévios


Python 3.8+

PostgreSQL (ou banco de dados relacional preferido)

Git

Bibliotecas Python

requests - Para realizar chamadas à API

pandas - Para manipulação de dados

sqlalchemy - Para integração com o banco de dados

logging - Para rastrear a execução do pipeline

## Instruções de Configuração

Clonar o Repositório

git clone https://github.com/username/etl-api-project.git
cd etl-api-project

## Instalar Dependências

pip install -r requirements.txt

## Configurar Variáveis de Ambiente

Crie um arquivo .env no diretório raiz e adicione o seguinte:

API_URL=<seu_endpoint_da_api>
API_KEY=<sua_chave_de_api>
DB_HOST=<seu_host_do_banco_de_dados>
DB_PORT=<sua_porta_do_banco_de_dados>
DB_USER=<seu_usuario_do_banco_de_dados>
DB_PASSWORD=<sua_senha_do_banco_de_dados>
DB_NAME=<seu_nome_do_banco_de_dados>

## Estrutura do Projeto

project-root/
|
|-- etl_pipeline.py         # Script principal para executar o processo ETL
|-- config.py               # Arquivo de configuração para variáveis de ambiente
|-- requirements.txt        # Lista de dependências Python
|-- .env                    # Variáveis de ambiente (não incluídas no repositório)
|-- README.md               # Documentação do projeto
|-- logs/                   # Pasta para arquivos de log
`-- tests/                  # Testes unitários para os componentes do ETL

## Processo ETL

1. Extração

Requisições à API: Busca de dados usando a biblioteca requests.

Tratamento de Erros: Registra erros e tenta novamente caso as chamadas à API falhem.

2. Transformação

Limpeza de Dados: Remove valores nulos, duplicados e entradas inválidas.

Normalização: Converte os dados para um formato consistente (por exemplo, formatos de data, intervalos numéricos).

Enriquecimento: Adiciona colunas derivadas ou agregados, se necessário.

3. Carregamento

Conexão com o Banco de Dados: Estabelece uma conexão com o banco de dados usando sqlalchemy.

Inserção de Dados: Carrega os dados transformados na tabela de destino do banco de dados.

## Como Executar

Executar o Pipeline ETL

python etl_pipeline.py

Agendar o Pipeline

Use uma ferramenta de agendamento como cron (Linux/Mac) ou o Agendador de Tarefas (Windows):

Exemplo de tarefa cron para executar o script diariamente à meia-noite:

0 0 * * * /usr/bin/python3 /path/to/etl_pipeline.py

Registro e Monitoramento

Os logs são armazenados no diretório logs/.

Os logs capturam:

Status das requisições à API

Etapas de transformação de dados

Erros e exceções

Testes

Execute os testes unitários usando:

pytest tests/


