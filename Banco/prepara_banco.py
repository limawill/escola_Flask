import sqlite3
import json
from dynaconf import settings


def criar_tabelas(self):
    conn = sqlite3.connect("alunos.sqlite")
    cursor = conn.cursor()
    # Execute the DROP Table SQL statement
    try:
        dropTable = "DROP TABLE alunos"
        cursor.execute(dropTable)
        conn.commit()
    except sqlite3.OperationalError:
        pass
    try:
        criar_tabelas = """CREATE TABLE "alunos" (
                        "cpf" TEXT NOT NULL UNIQUE,
                        "nome" TEXT NOT NULL, "sexo" TEXT NOT NULL,
                        "data_nasc" TEXT NOT NULL,"endereco" TEXT NOT NULL,
                        "complemento" TEXT,"cep" TEXT NOT NULL,
                        "anoletivo" INTEGER NOT NULL, "nota" INTEGER NOT NULL,
                        "mae" TEXT NOT NULL, "pai" TEXT,
                        "telefone" TEXT NOT NULL,
                        "email" TEXT NOT NULL,PRIMARY KEY("cpf"))"""
        cursor.execute(criar_tabelas)
    except sqlite3.OperationalError:
        pass

    # commitando senão nada tem efeito
    conn.commit()
    cursor.close()


def insere_massa(self):
    conn = sqlite3.connect("alunos.sqlite")
    cursor = conn.cursor()
    with open(settings.arquivoMassa, 'r') as myfile:
        data = myfile.read()

    json_data = json.loads(data)
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
        try:
            cursor.execute(settings.sqlInsert, (insert_aluno))
            conn.commit()
            insert_aluno.clear()
        except sqlite3.IntegrityError:
            conn.rollback()
            return "404"

    # Fechando conexão
    insert_aluno.clear()
    conn.close()
    return "OK"
