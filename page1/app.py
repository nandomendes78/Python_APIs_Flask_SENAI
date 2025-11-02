from flask import Flask, jsonify

app = Flask(__name__)

# Lista de Frutas
lista_de_frutas = [
    'Manga',
    'Morango',
    'Banana',
    'Pera',
    'uva'
]

# Definir Links


@app.route('/')
def home():
    return 'Minha primeira API! Acesse: /frutas'


@app.route('/frutas')
def listar_frutas():
    return jsonify(lista_de_frutas)


if __name__ == '__main__':
    app.run(debug=True)
