from flask import Flask, jsonify

api = Flask(__name__)

lista_de_filmes = [
    "Top Gun: Maverick",
    "Jogada de Rei",
    "O Menino que Descobriu o Vento",
    "A Sociedade da Neve",
    "Repetente",
    "O Menino de Pijama Listrado"

]

@api.route('/')
def home():
    return 'Minha segunda API está no ar! Acesse: /filmes'

@api.route('/filmes')
def get_filmes():
    return jsonify(lista_de_filmes)

if __name__ == '__main__':
    api.run(debug=True)