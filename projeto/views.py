from projeto import app, db
from flask import render_template, url_for, request

from projeto.models import Teste

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/teste', methods=['GET', "POST"])
def testepage():
    context = {}
    if request.method == "GET":
        pesquisa = request.args.get('pesquisa')
        print('GET:', pesquisa)
        context.update({'pesquisa': pesquisa})
    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']
        
        teste = Teste(
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )
        db.session.add(teste)
        db.session.commit()

    return render_template('teste.html', context=context)