from flask import Flask, render_template, request, redirect, flash, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = "qualquerthing45#"
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/bim3g1"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQL_ALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
db.init_app(app)
migrate = Migrate(app,db)
from models import Usuario, Pizza, Pedido
from modulos.usuarios.usuario import bp_usuario
from modulos.pizzas.pizzas import bp_pizzas
app.register_blueprint(bp_usuario, url_prefix='/usuarios')
app.register_blueprint(bp_pizzas, url_prefix='/pizzas')
from modulos.pedidos.pedidos import bp_pedidos
app.register_blueprint(bp_pedidos, url_prefix='/pedidos')

@app.route('/')
def index():
    return render_template("ola.html")