import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/cadastro', methods=['POST'])
def cadastro():
    json = request.get_json()
    nome = json['nome'].upper()
    sobrenome = json['sobrenome'].upper()
    posicao = json['posicao'].upper()
    return jsonify(nome=nome,sobrenome=sobrenome,posicao=posicao)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port,debug=True)