import sqlite3
import json
from dynaconf import settings


def db_connection():
    """Classe utilizada para abir a conexão com o banco"""
    try:
        conn = sqlite3.connect('alunos.sqlite')
    except sqlite3.Error as erro_conexao:
        print(erro_conexao)
    return conn


def insere_banco(alunos):
    connection = db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(settings.sqlInsert, (alunos))
        connection.commit()
        connection.close()
        return "OK"
    except sqlite3.IntegrityError:
        print("CPF Cadastrado")
        return "CPF Cadastrado"


def deletar_aluno(id):
    connection = db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(settings.sqlDelete, (id,))
        connection.commit()
        connection.close()
        return "OK"
    except sqlite3.IntegrityError:
        print("CPF Cadastrado")
        return "CPF Cadastrado"


def atualiza_dados(alunos):
    connection = db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(settings.sqlUpdate, (alunos[1], alunos[2], alunos[3],
                                            alunos[4], alunos[5], alunos[6],
                                            alunos[7], alunos[8], alunos[9],
                                            alunos[10], alunos[11], alunos[12],
                                            alunos[0]))
        connection.commit()
        connection.close()
        return "OK"
    except sqlite3.IntegrityError:
        print("CPF Cadastrado")
        return "CPF Cadastrado"


def lista_alunos():
    connection = db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(settings.slqListAll)
        lista = cursor.fetchall()
        return lista
    except sqlite3.IntegrityError:
        print("Problemas de conexão")
        return "Error"


def sexo_alunos(parametro):
    connection = db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(settings.sqlSexo, (parametro,))
        lista = cursor.fetchall()
        if lista is not None:
            return lista
        else:
            return "404"
    except sqlite3.IntegrityError:
        print("Problemas de conexão")
        return "Error"


def ano_alunos(parametro):
    connection = db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(settings.sqlNascimento,  ("%" + parametro + "%",))
        lista = cursor.fetchall()
        if lista is not None:
            return lista
        else:
            return "404"
    except sqlite3.IntegrityError:
        print("Problemas de conexão")
        return "Error"


def letivo_alunos(parametro):
    connection = db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(settings.sqlAnoLetivo, (parametro,))
        lista = cursor.fetchall()
        if lista is not None:
            return lista
        else:
            return "404"
    except sqlite3.IntegrityError:
        print("Problemas de conexão")
        return "Error"


def notas_alunos(parametro):
    connection = db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(settings.sqlNotas, (parametro,))
        lista = cursor.fetchall()
        if lista is not None:
            return lista
        else:
            return "404"
    except sqlite3.IntegrityError:
        print("Problemas de conexão")
        return "Error"
