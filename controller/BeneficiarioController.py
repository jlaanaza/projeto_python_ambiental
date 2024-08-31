from flask import Flask, request, jsonify
from service.BeneficiarioService import *

app = Flask(__name__)

class BeneficiarioController:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):
        self.app.add_url_rule('/beneficiarios', 'beneficiario_listar', self.beneficiario_listar, methods=['GET'])
        self.app.add_url_rule('/beneficiarios/<int:id>', 'beneficiario_obter', self.beneficiario_obter, methods=['GET'])
        self.app.add_url_rule('/beneficiarios', 'beneficiario_inserir', self.beneficiario_inserir, methods=['POST'])
        self.app.add_url_rule('/beneficiarios/<int:id>', 'beneficiario_atualizar', self.beneficiario_atualizar, methods=['PUT'])
        self.app.add_url_rule('/beneficiarios/<int:id>', 'beneficiario_deletar', self.beneficiario_deletar, methods=['DELETE'])

    def beneficiario_listar(self):
        beneficiarios = listar_beneficiarios()
        return jsonify([{'id': beneficiario[0], 'nome': beneficiario[5] if beneficiario[5] else beneficiario[1],
                         'cpf_cnpj': beneficiario[2], 'tipo': beneficiario[3]} for beneficiario in beneficiarios])    

    def beneficiario_obter(self,id):
        beneficiario = obter_beneficiario(id)        
        if beneficiario:
            return jsonify({'id': beneficiario[0], 'nome': beneficiario[5] if beneficiario[5] else beneficiario[1],
                             'cpf_cnpj': beneficiario[2], 'tipo': beneficiario[3]})
        else:
            return jsonify({'erro': 'Beneficiario não encontrado.'}), 404
    
    def beneficiario_inserir(self):      
        if(cadastrar_beneficiario(request.json)):            
            return jsonify({'mensagem': 'Beneficiario criado com sucesso!'}), 201
        else:
            return jsonify({'erro': 'Erro ao criar beneficiario.'}), 400        
        
    def beneficiario_atualizar(self, id):
        dados = request.json
    
        if(atualizar_beneficiario(dados, id)):
            return jsonify({'mensagem': 'Beneficiario atualizado com sucesso!'})
        else:
            return jsonify({'erro': 'Beneficiario não encontrado.'}), 404
    

    def beneficiario_deletar(self, id):
        if(deletar_beneficiario(id)):            
            return jsonify({'mensagem': 'Beneficiario removido com sucesso!'})
        else:
            return jsonify({'erro': 'Beneficiario não encontrado.'}), 404