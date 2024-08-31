# controller/EnderecoController.py
from flask import request, jsonify
from service.EnderecoService import *

class EnderecoController:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):
        self.app.add_url_rule('/enderecos', 'endereco_listar', self.endereco_listar, methods=['GET'])
        self.app.add_url_rule('/enderecos/<int:id>', 'endereco_obter', self.endereco_obter, methods=['GET'])
        self.app.add_url_rule('/enderecos', 'endereco_inserir', self.endereco_inserir, methods=['POST'])
        self.app.add_url_rule('/enderecos/<int:id>', 'endereco_atualizar', self.endereco_atualizar, methods=['PUT'])
        self.app.add_url_rule('/enderecos/<int:id>', 'endereco_deletar', self.endereco_deletar, methods=['DELETE'])

    def endereco_listar(self):
        enderecos = listar_enderecos()
        return jsonify([{'id': endereco[0], 'logradouro': endereco[1], 'cidade': endereco[2], 
                         'estado': endereco[3], 'cep': endereco[4]} for endereco in enderecos])

    def endereco_obter(self, id):
        endereco = obter_endereco(id)
        if endereco:
            return jsonify({'id': endereco[0], 'logradouro': endereco[1], 'cidade': endereco[2], 
                            'estado': endereco[3], 'cep': endereco[4]})
        else:
            return jsonify({'erro': 'Endereço não encontrado.'}), 404

    def endereco_inserir(self):
        if cadastrar_endereco(request.json):
            return jsonify({'mensagem': 'Endereço criado com sucesso!'}), 201
        else:
            return jsonify({'erro': 'Erro ao criar endereço.'}), 400

    def endereco_atualizar(self, id):
        if atualizar_endereco(request.json, id):
            return jsonify({'mensagem': 'Endereço atualizado com sucesso!'})
        else:
            return jsonify({'erro': 'Endereço não encontrado.'}), 404

    def endereco_deletar(self, id):
        if deletar_endereco(id):
            return jsonify({'mensagem': 'Endereço removido com sucesso!'})
        else:
            return jsonify({'erro': 'Endereço não encontrado.'}), 404
