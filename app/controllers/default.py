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

@app.route('/ordenacao/<campo>/<ordem_anterior>')
def ordenacao(campo='id', ordem_anterior=''):
	if campo == 'id':
		if ordem_anterior == campo:
			pessoas = Pessoa.query.order_by(Pessoa.id.desc()).all()
		else:
			pessoas = Pessoa.query.order_by(Pessoa.id).all()
	elif campo == 'nome':
		if ordem_anterior == campo:
			pessoas = Pessoa.query.order_by(Pessoa.nome.desc()).all()
		else:
			pessoas = Pessoa.query.order_by(Pessoa.nome).all()
	elif campo == 'idade':
		if ordem_anterior == campo:
			pessoas = Pessoa.query.order_by(Pessoa.idade.desc()).all()
		else:
			pessoas = Pessoa.query.order_by(Pessoa.idade).all()		
	elif campo == 'sexo':
		if ordem_anterior == campo:
			pessoas = Pessoa.query.order_by(Pessoa.sexo.desc()).all()
		else:
			pessoas = Pessoa.query.order_by(Pessoa.sexo).all()
	elif campo == 'salario':
		if ordem_anterior == campo:
			pessoas = Pessoa.query.order_by(Pessoa.salario.desc()).all()
		else:
			pessoas = Pessoa.query.order_by(Pessoa.salario).all()
	else:
		pessoas = Pessoa.query.order_by(Pessoa.id).all()

	return render_template('listagem.html', pessoas=pessoas, ordem=campo)	

@app.route('/consulta', methods=['POST'])
def consulta():
	consulta = '%'+request.form.get('consulta')+'%'
	campo = request.form.get('campo')

	if campo == 'nome':
		pessoas = Pessoa.query.filter(Pessoa.nome.like(consulta)).all()
	elif campo == 'idade':
		pessoas = Pessoa.query.filter(Pessoa.idade.like(consulta)).all()
	elif campo == 'sexo':
		pessoas = Pessoa.query.filter(Pessoa.sexo.like(consulta)).all()
	elif campo == 'salario':
		pessoas = Pessoa.query.filter(Pessoa.salario.like(consulta)).all()
	else:
		pessoas = Pessoa.query.all()

	return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route('/insercao')
def insercao():
	return render_template('insercao.html')

@app.route('/salvar_insercao', methods=['POST'])
def salvar_insercao():
	Nome = request.form.get('nome')
	Idade = int(request.form.get('idade'))
	Sexo = request.form.get('sexo')
	Salario = float(request.form.get('salario'))

    #Instancia pessoa
	pessoa = Pessoa(Nome, Idade, Sexo, Salario)

    #Adiciona registro de Pessoa no banco de dados
	db.session.add(pessoa)
	db.session.commit()

	pessoas = Pessoa.query.all()
	return render_template('listagem.html', pessoas=pessoas, ordem='id')

