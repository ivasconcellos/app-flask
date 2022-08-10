from flask import render_template, request
from app import app, db
from app.models.tables import Pessoa

#As duas rotas apontam para o mesmo local (duas rotas seguidas)
@app.route('/')
@app.route('/listagem')
def listagem():
	pessoas = Pessoa.query.all()
	return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route('/selecao/<int:id>')
def selecao(id=0):
	pessoas = Pessoa.query.filter_by(id=id).all()
	return render_template('listagem.html', pessoas=pessoas, ordem='id')

