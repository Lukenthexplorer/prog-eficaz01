from flask import Flask, render_template, request, url_for, redirect
from utils import BancoDados


app = Flask(__name__)
db = BancoDados()


@app.route('/')
def home():
    return render_template('index.html', notas=db.get_notes())


@app.route('/notes', methods=['POST'])
def add_note():
    titulo = request.form['titulo']
    detalhes = request.form['detalhes']

    db.add_note(title=titulo, details=detalhes)

    return redirect(url_for('home'))


@app.route('/notes/<int:id>/delete', methods=['POST'])
def delete_note(id):
    db.delete_note(id)
    return redirect(url_for('home'))


@app.route('/notes/<int:id>/edit', methods=['GET', 'POST'])
def edit_note(id):
    if request.method == 'POST':
        titulo = request.form['titulo']
        detalhes = request.form['detalhes']
        db.update_note(id, title=titulo, details=detalhes)
        return redirect(url_for('home'))

    nota = db.get_note(id)
    return render_template('edit.html', nota=nota)


if __name__ == "__main__":
    app.run(debug=True)