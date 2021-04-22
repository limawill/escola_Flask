# Desafio API ESCOLA

Este projeto é executado no micro framework Python: Flask e banco de dados SQLite

## Dependencias

- Flask==1.1.2
- dynaconf==3.1.4


## Como rodar localmente
0 app será executado dentro e um container Docker para instalação do mesmo há estes tutoriais:<p>
https://docs.docker.com/docker-for-windows/install/ </p>
<p>https://fedoramagazine.org/docker-and-fedora-32/https://fedoramagazine.org/docker-and-fedora-32/</p>

### Docker

Com o docker instalado e os arquivos já copiados na sua maquina, rodar os seguintes comandos:
```sh
docker build -t escola .
```
Após a compilação:
```sh
docker run -d -p 5000:5000 escola
```
Caso não tenha nenhum problema rodando o comando:
```sh
docker ps -a
```
Terá uma saida semelhante a está
```sh
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS         PORTS                    NAMES
292e3f98c6f4   flask     "flask run"   4 seconds ago   Up 2 seconds   0.0.0.0:5000->5000/tcp   gifted_brahmagupta
```
E no seu navegador de preferencia acessar:
```sh
http://127.0.0.1:5000/
```

## URL's de acesso a funções
Após o flask estar ativo acesse:
```sh
http://127.0.0.1:5000
```
### URL /candidates
```sh
http://127.0.0.1:5000/candidates
```
Esta URL é responde a solicitação do **Alfi** a de inclusão de novos usuarios, é verificado pelo CNPJ se o cadastro já existe caso não o mesmo inclui, se já existir é informado no retorno que o usuario já existe. Para simulação os dados do usuario vem do arquivo: **dadosCadastros.json**

### URL /candidates/1
```sh
http://127.0.0.1:5000/candidates/1
```
Esta URL é responde a solicitação do **Samuca** a de realizar o update dos usuarios que estão na base de dados, atualizando somente os campos:
- Nome
- Sobrenome
- Tipo do contato
- Telefone

A realização da atualização é realizado pela verificação do CNPJ na base. O retorno infoma quantos usuarios foram atualizados com sucesso cadastro. 
Para simulação os dados dos usuarios vem do arquivo: **dadosAlterados.json**


### URL /contacts
```sh
http://127.0.0.1:5000/contacts
```
Esta URL é responde a uma das solicitações do **Fabricio** a de verificação dos novos canditados (usuarios), automaticamente ele retorna no formato **json** todos os usuarios cadastrados no dia da pesquisa.
É possivel realizar pesquisa por periodo, basta incluir na URL um endpoint, conforme o exemplo abaixo:

```sh
http://127.0.0.1:5000/contacts?numberDays=4
```
No exemplo acima a busca será realizada da data atual há 4 dias atrás (Ex: do dia 05/04 até 09/05)


### URL /contacts/1

```sh
http://127.0.0.1:5000/contacts/1
```
Esta URL é responde a outra solicitação feita pelo **Fabricio** a de verificação na atualização dos dados dos canditados (usuarios), automaticamente ele retorna no formato **json** todos os usuarios que atualizaram seus dados no dia da pesquisa.
É possivel realizar pesquisa por periodo, basta incluir na URL um endpoint, conforme o exemplo abaixo:

```sh
http://127.0.0.1:5000/contacts/1?numberDays=4
```
No exemplo acima a busca será realizada da data atual há 4 dias atrás (Ex: do dia 05/04 até 09/05)

## Estrutura do projeto
```sh
.
├── app.py
├── Banco
│   ├── executa_banco.py
│   ├── __init__.py
│   └── prepara_banco.py
├── Dados
│   ├── Altera.json
│   ├── Cadastro.json
│   └── MassaDados.json
├── Dockerfile
├── requirements.txt
├── settings.toml
└── views.py

```

