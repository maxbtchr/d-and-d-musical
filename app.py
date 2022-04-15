from flask import Flask, render_template
from pip import main

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('accueil.html', page_title='Accueil')

@app.route('/accueil')
def accueil():
    return render_template('accueil.html', page_title='Accueil')

@app.route('/creation')
def creation():
    return render_template('creation.html', page_title='Creation')

@app.route('/personnages-crees')
def creation():
    return render_template('personnages-crees.html', page_title='Personnages Crees')

@app.route('/personnage-par-defaut')
def creation():
    return render_template('personnage-par-defaut.html', page_title='Personnage-Par-Defaut')

if __name__ == "__main__":
    app.run(debug=true)