# controller/AlimentoController.py
from flask import request, jsonify
from service.AlimentoService import *

class AlimentoController:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):
        self.app.add_url_rule('/alimentos', 'alimento_listar', self.alimento_listar, methods=['GET'])
        self.app.add_url_rule('/alimentos/<int:id>', 'alimento_obter', self.alimento_obter, methods=['GET'])
        self.app.add_url_rule('/alimentos', 'alimento_inserir', self.alimento_inserir, methods=['POST'])
        self.app.add_url_rule('/alimentos/<int:id>', 'alimento_atualizar', self.alimento_atualizar, methods=['PUT'])
        self.app.add_url_rule('/alimentos/<int:id>', 'alimento_deletar', self.alimento_deletar, methods=['DELETE'])

    def alimento_listar(self):
        alimentos = listar_alimentos()
        return jsonify([{
            'nome': alimento[0],
            'quantidade': alimento[1],
            'perecivel': bool(alimento[2]),
            'data_validade': alimento[3],
            'nome_colaborador': alimento[4] if alimento[4] else alimento[9] if alimento[9] else "Anônimo",
            'logradouro': alimento[5],
            'cidade': alimento[6],
            'estado': alimento[7],
            'cep': alimento[8]
        } for alimento in alimentos])


    def alimento_obter(self, id):
        alimento = obter_alimento(id)
        if alimento:
            return jsonify({
                'nome': alimento[0],
                'quantidade': alimento[1],
                'perecivel': bool(alimento[2]),
                'data_validade': alimento[3],
                'nome_colaborador': alimento[4] if alimento[4] else alimento[9] if alimento[9] else "Anônimo",
                'logradouro': alimento[5],
                'cidade': alimento[6],
                'estado': alimento[7],
                'cep': alimento[8]
            })
        else:
            return jsonify({'erro': 'Alimento não encontrado.'}), 404

    def alimento_inserir(self):
        sucesso, mensagem = cadastrar_alimento(request.json)
        if sucesso:
            return jsonify({'mensagem': mensagem}), 201
        else:
            return jsonify({'erro': mensagem}), 400

    def alimento_atualizar(self, id):
        sucesso, mensagem = atualizar_alimento(request.json, id)
        if sucesso:
            return jsonify({'mensagem': 'Alimento atualizado com sucesso!'}),200
        elif mensagem:
            return jsonify({'erro': mensagem}), 400
        else:
            return jsonify({'erro':"Alimento não encontrado"}), 404

    def alimento_deletar(self, id):
        if deletar_alimento(id):
            return jsonify({'mensagem': 'Alimento removido com sucesso!'})
        else:
            return jsonify({'erro': 'Alimento não encontrado.'}), 404
