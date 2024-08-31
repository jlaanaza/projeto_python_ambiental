from flask import Flask, request, jsonify
from service.ColaboradorService import *

app = Flask(__name__)

class ColaboradorController:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):
        self.app.add_url_rule('/colaboradores', 'colaborador_listar', self.colaborador_listar, methods=['GET'])
        self.app.add_url_rule('/colaboradores/<int:id>', 'colaborador_obter', self.colaborador_obter, methods=['GET'])
        self.app.add_url_rule('/colaboradores', 'colaborador_inserir', self.colaborador_inserir, methods=['POST'])
        self.app.add_url_rule('/colaboradores/<int:id>', 'colaborador_atualizar', self.colaborador_atualizar, methods=['PUT'])
        self.app.add_url_rule('/colaboradores/<int:id>', 'colaborador_deletar', self.colaborador_deletar, methods=['DELETE'])

    def colaborador_listar(self):
        colaboradores = listar_colaboradores()
        return jsonify([{'id': colaborador[0], 'nome': colaborador[5] if colaborador[5] else colaborador[1],
                         'cpf_cnpj': colaborador[2], 'tipo': colaborador[3]} for colaborador in colaboradores])    

    def colaborador_obter(self,id):
        colaborador = obter_colaborador(id)        
        if colaborador:
            return jsonify({'id': colaborador[0], 'nome': colaborador[5] if colaborador[5] else colaborador[1],
                             'cpf_cnpj': colaborador[2], 'tipo': colaborador[3]})
        else:
            return jsonify({'erro': 'Colaborador não encontrado.'}), 404
    
    def colaborador_inserir(self):      
        if(cadastrar_colaborador(request.json)):            
            return jsonify({'mensagem': 'Colaborador criado com sucesso!'}), 201
        else:
            return jsonify({'erro': 'Erro ao criar colaborador.'}), 400        
        
    def colaborador_atualizar(self, id):
        dados = request.json
    
        if(atualizar_colaborador(dados, id)):
            return jsonify({'mensagem': 'Colaborador atualizado com sucesso!'})
        else:
            return jsonify({'erro': 'Colaborador não encontrado.'}), 404
    

    def colaborador_deletar(self, id):
        if(deletar_colaborador(id)):            
            return jsonify({'mensagem': 'Colaborador removido com sucesso!'})
        else:
            return jsonify({'erro': 'Colaborador não encontrado.'}), 404