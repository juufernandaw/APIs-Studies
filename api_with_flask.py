# API: Lugar onde é disponibilizado recursos/funcionalidades
# 1. Objetivo: Criar um api que disponibiliza crud de livros
# 2. Url base: localhost
# 3. Endpoints:
#  - localhost/livros (GET) -> consulta por todos os livros
#  - localhost/livros/id (GET) -> consulta por um livro pelo id
#  - localhost/livro/id (PUT) -> alterar um registro de livro
#  - localhost/livro/id (DELETE) -> excluir um registro de livro
#  - localhost/livro/id (POST) -> criar um registro de livro

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Harry P.',
        'autor': 'J.K.R'
    },
    {
        'id': 2,
        'titulo': 'A Menina',
        'autor': 'Joana'
    }
]


# Consultar(todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


# Consultar(id)
@app.route('/livros/<int:id>',  methods=['GET'])  # espero um número do tipo inteiro menor e maior que o inteiro dado, ou seja, igual
def obter_livro_por_id(id: str):
    for livro in livros:
        if livro["id"] == id:
            return jsonify(livro)


# Editar
@app.route('/livros/<int:id>',  methods=['PUT'])
def editar_livro_por_id(id: str):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro["id"] == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])


# Criar
@app.route('/livros', methods=['POST'])
def incluir_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)


# Excluir
@app.route('/livros/<int:id>',  methods=['DELETE'])
def excluir_livro(id: str):
    for indice, livro in enumerate(livros):
        if livro["id"] == id:
            del livros[indice]
    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
