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
### URL /cadastro
```sh
http://127.0.0.1:5000/cadastro
```
Esta URL é responde a solicitação de inclusão de novos alunos, é verificado pelo CPF se o aluno já existe caso não o mesmo inclu. Caso o aluno já esteja cadastrado retorna a código **404**, caso o mesmo seja incluido na base de dados o retorno é **200**. Para simulação os dados do usuario tem a sua origem do  arquivo: **Cadastro.json**

### URL /atualizar
```sh
http://127.0.0.1:5000/atualizar
```
Esta URL é responde a solicitação para alteração de dados dos alunos, é verificado pelo CPF se o aluno não existe na base de dados retorna a código **404**. Caso o mesmo seja encontrado seus dados são atualizados e o código de retorno é **200**. Para simulação os dados do usuario tem a sua origem do  arquivo: **Altera.json**

### URL /listar
```sh
http://127.0.0.1:5000/listar
```
Esta URL é responde a solicitação para listagem de todos os alunos  cadastrados. A saída dos dados está no formatdo **JSON**

### URL /remover + CPF
```sh
http://127.0.0.1:5000/remover?CPF=356.520.020-00
```
Esta URL é responde a solicitação para exclusão de um aluno da base de dados. Para realizar a exclusão é necessario informar o CPF do aluno, caso o mesmo não seja informado retorna a mensagem **CPF not found - 404".*** Informando o CPF o sistema faz a busca na base de dados e retorna a código **404** caso não seja encontrado, e o o retorno positivo é **200** 

### URL /filtrar/

Foi implementado filtros basicos do Sexo, ano de nascimento, nota e ano letivo do aluno. Para todos os casos é necessario informar o dado que deseja buscar (veja exemplos abaixo). Caso não seja informado retorna o código ***404***. A saída dos dados está no formatdo **JSON**

#### Sexo do Aluno 
```sh
http://127.0.0.1:5000/filtrar/sexo?SEXO=Feminino
```

#### Ano de Nascimento 
```sh
http://127.0.0.1:5000/filtrar/AnoNasc?NASC=2003
```
#### Ano letivo (série)
```sh
127.0.0.1:5000/filtrar/anoletivo?LETIVO=6
```
#### Nota do Aluno 
```sh
http://127.0.0.1:5000/filtrar/Nota?NOTA=5
```

### URL /massa

Foi implementado somente para ter um resultado maior na aplicação dos filtros. Para simulação os dados do usuario tem a sua origem do  arquivo: **MassaDados.json**

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

