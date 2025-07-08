from projeto import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/teste')
def testepage():
    return "oi 2.0"