# TACO API FOODS SERVICE

### Descrição

Esse projeto é um Microserviço criado para pesquisa de alimentos a partir da tabela TACO

## Tecnologias

* FastAPI
* MongoDB (beanie)
* Python 3.12

## Observações

Antes de iniciar, você deve criar um arquivo .env na raiz do projeto para estabelecer os valores de banco de dados e messageria.

| Variável | Descrição |
| -------- | ------- |
| DB_HOST  | Host de conexão do MongoDB |
| DB_NAME | Nome da base de dados a ser utilizada |
| DB_USERNAME | Nome do usuário do banco de dados |
| DB_PASSWORD | Senha de acesso ao banco de dados |
| APP_VERSION | Versão da aplicação |

OBS: Foi usado MongoDB Cloud para realizar o desenvolvimento desse projeto

## Inicialização

* Pode ser realizado via execução direta com python main.py
* Ou então através da criação de um container usando do Dockerfile disponível

