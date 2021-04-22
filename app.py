""" Inicio do APP importando FLASK"""
from flask import Flask
import views
from Banco.prepara_banco import criar_tabelas


def create_app():
    """Classe Inicial """
    app = Flask(__name__)
    views.configure(app)
    criar_tabelas(app)
    return app
