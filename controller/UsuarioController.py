from flask import Flask, request, jsonify
from service.UsuarioService import listar_usuarios,obter_usuario,atualizar_usuario,deletar_usuario

app = Flask(__name__)

class UsuarioController:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):
        self.app.add_url_rule('/usuarios', 'listar', self.listar, methods=['GET'])
        self.app.add_url_rule('/usuarios/<int:id>', 'obter', self.obter, methods=['GET'])
        self.app.add_url_rule('/usuarios/<int:id>', 'atualizar', self.atualizar, methods=['PUT'])
        self.app.add_url_rule('/usuarios/<int:id>', 'deletar', self.deletar, methods=['DELETE'])

    def listar(self):
        usuarios = listar_usuarios()
        return jsonify([{'id': usuario[0], 'nome': usuario[1], 'cpf_cnpj': usuario[2], 'tipo': usuario[3]} for usuario in usuarios])    

    def obter(self,id):
        usuarios = obter_usuario(id)        
        if usuarios:
            return jsonify({'id': usuarios[0], 'nome': usuarios[1], 'cpf_cnpj': usuarios[2], 'tipo': usuarios[3]})
        else:
            return jsonify({'erro': 'Usuario não encontrado.'}), 404
        
    def atualizar(self, id):
        dados = request.json
        
        if(atualizar_usuario(dados, id)):
            return jsonify({'mensagem': 'Usuário atualizado com sucesso!'})
        else:
            return jsonify({'erro': 'Usuario não encontrado.'}), 404
    

    def deletar(self, id):
        if(deletar_usuario(id)):            
            return jsonify({'mensagem': 'Usuário removido com sucesso!'})
        else:
            return jsonify({'erro': 'Usuario não encontrado.'}), 404