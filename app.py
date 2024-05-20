from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

clientes = [
    {'cpf': '12345678901', 'nm_cliente': 'Tete', 'email': 'tete@exemplo.com', 'tipo_deficiencia': 'auditiva'},
]


@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    return jsonify(clientes)


@app.route('/api/clientes', methods=['POST'])
def create_cliente():
    try:
        novo_cliente = request.get_json()
        clientes.append(novo_cliente)
        return jsonify(novo_cliente), 201
    except Exception as e:
        print(f"Erro ao criar cliente: {e}")
        return jsonify({"message": "Erro interno do servidor"}), 500


if __name__ == '__main__':
    app.run(debug=True)
