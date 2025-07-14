from projeto import app, db
from flask import render_template, url_for, request, redirect

from projeto.models import Teste
from projeto.forms import TesteForm

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/teste', methods=['GET', "POST"])
def teste():
    form = TesteForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))

    return render_template('teste.html', context=context,  form=form)

#formato antigo(incorreto)

@app.route('/teste_old', methods=['GET', "POST"])
def teste_old():
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

    return render_template('teste_old.html', context=context)