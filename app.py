from flask import Flask, render_template
from pip import main

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('accueil.html', page_active='accueil')

@app.route('/accueil')
def accueil():
    return render_template('accueil.html', page_active='accueil')

@app.route('/creation')
def creation():
    return render_template('creation.html', page_active='creation')

@app.route('/personnages-crees')
def personnages_crees():
    return render_template('personnages-crees.html', page_active='personnages_crees')

@app.route('/personnage-par-defaut')
def personnage_par_defaut():
    return render_template('personnage-par-defaut.html', page_active='personnage_par_defaut')

if __name__ == "__main__":
    app.run(debug=True)