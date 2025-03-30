from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/arcane-majeure/')
def majeure():
    return render_template('majeure.html')

@app.route('/batons/')
def batons():
    return render_template('batons.html')

@app.route('/coupes/')
def coupes():
    return render_template('coupes.html')

@app.route('/epees/')
def epees():
    return render_template('epees.html')

@app.route('/deniers/')
def deniers():
    return render_template('deniers.html')

@app.route('/mentionslegales/')
def mentionsLegales():
    return render_template('mention_legale.html')