# Projeto ETL: Extração de Dados de uma API

## Visão Geral do Projeto

Este projeto implementa um pipeline ETL (Extract, Transform, Load) para extrair dados de uma API externa, processá-los de acordo com os requisitos de negócio e armazenar os dados transformados em um banco de dados para análise posterior.

Além disso, o projeto inclui a integração com a API da OpenAI para gerar respostas de IA, o que pode ser útil em tarefas de análise de dados e processamento de linguagem natural.

## Principais Características

- **Extração**: Os dados são buscados de uma API externa (incluindo a OpenAI) usando requisições HTTP RESTful.
- **Transformação**: Os dados são limpos, normalizados e estruturados para atender aos requisitos de negócio.
- **Carregamento**: Os dados processados são armazenados em um banco de dados relacional para consultas e análises eficientes.
- **Integração com a OpenAI**: O código utiliza a API da OpenAI para gerar respostas de texto, com base em entradas fornecidas pelo usuário.

## Requisitos Prévios

- Python 3.8+
- PostgreSQL (ou banco de dados relacional preferido)
- Git
- Bibliotecas Python:
  - `requests` - Para realizar chamadas à API
  - `python-dotenv` - Para carregar variáveis de ambiente de forma segura
  - `pandas` - Para manipulação de dados
  - `sqlalchemy` - Para integração com o banco de dados
  - `logging` - Para rastrear a execução do pipeline

## Instruções de Configuração

### Clonar o Repositório

Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/username/etl-api-project.git
cd etl-api-project
```

## Instalar Dependências
## Instale as dependências do projeto listadas no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```
## Configurar Variáveis de Ambiente
Crie um arquivo .env no diretório raiz e adicione as seguintes variáveis de ambiente:

```env
API_URL=<seu_endpoint_da_api>
API_KEY=<sua_chave_de_api_openai>
DB_HOST=<seu_host_do_banco_de_dados>
DB_PORT=<sua_porta_do_banco_de_dados>
DB_USER=<seu_usuario_do_banco_de_dados>
DB_PASSWORD=<sua_senha_do_banco_de_dados>
DB_NAME=<seu_nome_do_banco_de_dados>
OPENAI_API_KEY=<sua_chave_de_api_openai>
Nota: Certifique-se de configurar a chave da API da OpenAI corretamente (OPENAI_API_KEY), que será usada para fazer requisições para o modelo de IA.
```

## Estrutura do Projeto
```plaintext
project-root/
|
|-- etl_pipeline.py         # Script principal para executar o processo ETL
|-- config.py               # Arquivo de configuração para variáveis de ambiente
|-- requirements.txt        # Lista de dependências Python
|-- .env                    # Variáveis de ambiente (não incluídas no repositório)
|-- README.md               # Documentação do projeto
|-- logs/                   # Pasta para arquivos de log
|-- tests/                  # Testes unitários para os componentes do ETL
```
## Processo ETL
1. Extração

Requisições à API: Busca de dados usando a biblioteca requests, incluindo a API da OpenAI para gerar respostas.
Tratamento de Erros: Registra erros e tenta novamente caso as chamadas à API falhem.

2. Transformação

Limpeza de Dados: Remove valores nulos, duplicados e entradas inválidas.
Normalização: Converte os dados para um formato consistente (por exemplo, formatos de data, intervalos numéricos).
Enriquecimento: Adiciona colunas derivadas ou agregados, se necessário.]

3. Carregamento

Conexão com o Banco de Dados: Estabelece uma conexão com o banco de dados usando sqlalchemy.
Inserção de Dados: Carrega os dados transformados na tabela de destino do banco de dados.

## Integração com a OpenAI
Este projeto inclui a capacidade de fazer requisições à API da OpenAI para obter respostas de IA. O seguinte código exemplifica como usar a API para gerar uma resposta a partir de uma entrada do usuário:

```python
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Quais as principais características de um bom analista de dados?"}]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# Verificando o status da resposta
if response.status_code == 200:
    try:
        # Tentar acessar a resposta
        print(response.json()["choices"][0]["message"]["content"])
        
    except KeyError:
        print("Erro: A estrutura do JSON retornado não contém a chave 'choices'.")
        print(response.json())  # Exibe a resposta completa para análise
else:
    print(f"Erro na API: status code {response.status_code}")
    print(response.json())  # Exibe a resposta de erro da API
```

Este código envia uma mensagem para a API da OpenAI e imprime a resposta gerada.

## Como Executar
Para rodar o pipeline ETL e fazer a requisição à API da OpenAI, execute o seguinte comando:

```bash
python etl_pipeline.py
```
## Agendar o Pipeline
Use uma ferramenta de agendamento como cron (Linux/Mac) ou o Agendador de Tarefas (Windows):

Exemplo de tarefa cron para executar o script diariamente à meia-noite:

```bash
0 0 * * * /usr/bin/python3 /path/to/etl_pipeline.py
```
## Registro e Monitoramento
Os logs são armazenados no diretório logs/. Eles capturam:

* Status das requisições à API
* Etapas de transformação de dados
* Erros e exceções

## Testes
Execute os testes unitários para verificar a integridade do processo ETL e da integração com a API:

```bash
pytest tests/
```
## Dependências
As dependências do projeto estão listadas no arquivo requirements.txt. Para instalar as dependências, use o seguinte comando:

```bash
pip install -r requirements.txt
```
## Arquivo ```requirements.txt:```
```txt
requests
python-dotenv
pandas
sqlalchemy
logging
```
## Contribuição
Sinta-se à vontade para contribuir com melhorias ou enviar issues para problemas encontrados.

## Licença
Este projeto é de código aberto e licenciado sob a Licença MIT.