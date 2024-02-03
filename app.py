from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

agenda = [
	{
		"nome": "Guido",
		"telefone": "71 9 8888-8888"
	}
]

@app.route('/listar', methods=['GET'])
def listar_agenda():
	return jsonify(agenda)

@app.route('/cadastrar', methods=['POST'])
def cadastrar_agenda():
	body = request.get_json()
	agenda.append(body)
	return make_response(body, 201)

@app.route('/obter/<nome>', methods=['GET'])
def obter_agenda(nome):
	encontrado = None
	for item in agenda:
		if item["nome"] == nome:
			encontrado = item
			break
	if not encontrado:
		return make_response('Telefone não encontrado.', 404)
	return jsonify(encontrado)

@app.route('/excluir/<nome>', methods=['DELETE'])
def excluir_agenda(nome):
	encontrado = None
	for item in agenda:
		if item["nome"] == nome:
			encontrado = item
			break
	if not encontrado:
		return make_response('Telefone não encontrado.', 404)
	agenda.remove(encontrado)
	return make_response('', 204)

@app.route('/atualizar/<nome>', methods=['PUT'])
def atualizar_agenda(nome):
	body = request.get_json()
	encontrado = None
	for item in agenda:
		if item["nome"] == nome:
			encontrado = item
			break
	if not encontrado:
		return make_response('Telefone não encontrado.', 404)
	encontrado.update(body)
	return make_response('', 204)

app.run(host='localhost', port=3000, debug=True)