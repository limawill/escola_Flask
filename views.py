"""Import para trabalhar com banco de dados SQLite"""
import sqlite3
import json
from dynaconf import settings
from flask import jsonify, request
from Banco.executa_banco import *
from Banco.prepara_banco import insere_massa


def abre_jason(dados_json):
    """Classe utilizada para abir arquivo JSON (Pode ser trocada por URL)"""
    with open(dados_json, 'r') as myfile:
        data = myfile.read()
    return json.loads(data)


def captura_dados(arquivo_json):
    json_data = abre_jason(arquivo_json)
    insert_aluno = []
    for i in json_data:
        insert_aluno.append(i["cpf"])
        insert_aluno.append(i["nome"])
        insert_aluno.append(i["sexo"])
        insert_aluno.append(i["data_nasc"])
        insert_aluno.append(i["endereco"])
        insert_aluno.append(i["complemento"])
        insert_aluno.append(i["cep"])
        insert_aluno.append(i["anoletivo"])
        insert_aluno.append(i["nota"])
        insert_aluno.append(i["filiacao"]["mae"])
        insert_aluno.append(i["filiacao"]["pai"])
        insert_aluno.append(i["contacts"]["telefone"])
        insert_aluno.append(i["contacts"]["email"])

    return insert_aluno


def configure(app):
    """Classe Principal do APP"""
    @app.route('/')
    def home():
        return "WORK"

    @app.route('/cadastro', methods=['GET'])
    def cadastro():
        aluno = captura_dados(settings.arquivoNovos)
        retorno = insere_banco(aluno)
        if retorno == "OK":
            return "200"
        else:
            return "404"

    @app.route('/remover', methods=['GET'])
    def remover():
        cpf = request.args.get('CPF')
        if cpf is not None:
            retorno = deletar_aluno(cpf)
            if retorno == "OK":
                return "200"
            else:
                return "404"
        else:
            return "CPF not found"

    @app.route('/atualizar', methods=['GET'])
    def atualizar():
        aluno = captura_dados(settings.arquivosAlterados)
        retorno = atualiza_dados(aluno)
        if retorno == "OK":
            return "200"
        else:
            return "404"

    @app.route('/listar', methods=['GET'])
    def listar():
        retorno = lista_alunos()
        if retorno is not None:
            return jsonify(retorno)
        else:
            return "404"

    @app.route('/filtrar/sexo', methods=['GET'])
    def filtrarSexo():
        sexo = request.args.get('SEXO')
        if sexo is not None:
            retorno = sexo_alunos(sexo)
            if retorno is not None:
                return jsonify(retorno)
            else:
                return "404"
        else:
            return "Sexo não informado"

    @app.route('/filtrar/AnoNasc', methods=['GET'])
    def filtrarAnoNasc():
        nascimento = request.args.get('NASC')
        if nascimento is not None:
            retorno = ano_alunos(nascimento)
            if retorno is not None:
                return jsonify(retorno)
            else:
                return "404"
        else:
            return "Ano não informado"

    @app.route('/filtrar/AnoLetivo', methods=['GET'])
    def filtrarAnoLetivo():
        ano_letivo = request.args.get('LETIVO')
        if ano_letivo is not None:
            retorno = letivo_alunos(ano_letivo)
            if retorno is not None:
                return jsonify(retorno)
            else:
                return "404"
        else:
            return "Ano não informado"

    @app.route('/filtrar/Nota', methods=['GET'])
    def filtrarNota():
        nota = request.args.get('NOTA')
        if nota is not None:
            retorno = notas_alunos(nota)
            if retorno is not None:
                return jsonify(retorno)
            else:
                return "404"
        else:
            return "Nota não informado"

    @app.route('/massa', methods=['GET'])
    def massa():
        retorno = insere_massa(app)
        if retorno == "OK":
            return "200"
        else:
            return "404"
