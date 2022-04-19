from flask import Flask, render_template
from pip import main

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('accueil.html', titre_page='Accueil')

@app.route('/accueil')
def accueil():
    return render_template('accueil.html', titre_page='Accueil')

@app.route('/creation')
def creation():
    return render_template('creation.html', titre_page='Création')

@app.route('/personnages-crees')
def personnages_crees():
    return render_template('personnages-crees.html', titre_page='Musiciens créés')

@app.route('/personnage-par-defaut')
def personnage_par_defaut():
    return render_template('personnage-par-defaut.html', titre_page='Musicien par défaut')

if __name__ == "__main__":
    app.run(debug=True)