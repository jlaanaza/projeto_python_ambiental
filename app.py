# main.py
from flask import Flask
from banco.DatabaseConnection import inicializar_banco
from controller.UsuarioController import UsuarioController
from controller.ColaboradorController import ColaboradorController
from controller.BeneficiarioController import BeneficiarioController
from controller.AlimentoController import AlimentoController
from controller.EnderecoController import EnderecoController

app = Flask(__name__)

inicializar_banco()

# Registrar controllers
usuario_controller = UsuarioController(app)
colaborador_controller = ColaboradorController(app)
beneficiario_controller = BeneficiarioController(app)
alimento_controller = AlimentoController(app)
endereco_controller = EnderecoController(app)

if __name__ == '__main__':
    app.run(debug=True)
