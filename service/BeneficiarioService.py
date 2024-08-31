from banco.DatabaseConnection import conectar_banco
from service.UsuarioService import cadastrar_usuario

def listar_beneficiarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT Usuario.id, Usuario.nome,Usuario.tipo, Usuario.cpf_cnpj, Usuario.tipo,' +
                    'Beneficiario.nome_beneficiario FROM Usuario  INNER JOIN Beneficiario ON Usuario.id = Beneficiario.id')
    beneficiarios = cursor.fetchall()
    conexao.close()
    return beneficiarios

def obter_beneficiario(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    beneficiarios = buscar_beneficiario(id, cursor)
    conexao.close()
    return beneficiarios

def cadastrar_beneficiario(dados):
    nome_beneficiario = dados.get('nome_beneficiario')  # Nome social ou pseudônimo

    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Criar o usuário primeiro
    usuario_id = cadastrar_usuario(dados)  # Obter o ID gerado para o usuário
    try:
        if(usuario_id):
            # Criar o beneficiario com o ID do usuário recém-criado
            cursor.execute('INSERT INTO Beneficiario (id, nome_beneficiario) VALUES (?, ?)', (usuario_id, nome_beneficiario))
            conexao.commit()
            return True
        else:
            return False
    finally:
        conexao.close()    

def atualizar_beneficiario(dados, id):
    nome = dados.get('nome')
    cpf_cnpj = dados.get('cpf_cnpj')
    tipo = dados.get('tipo')
    senha = dados.get('senha')
    nome_beneficiario = dados.get('nome_beneficiario')

    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        if(buscar_beneficiario(id, cursor)):       
            cursor.execute('UPDATE Usuario SET nome = ?, cpf_cnpj = ?, tipo = ?, senha = ? WHERE id = ?', (nome, cpf_cnpj, tipo, senha, id))
            cursor.execute('UPDATE Beneficiario SET nome_beneficiario = ? WHERE id = ?', (nome_beneficiario, id))
            conexao.commit()
            conexao.close()
            return True
        else :
            return False
    finally:
        conexao.close() 
    
def deletar_beneficiario(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        if(buscar_beneficiario(id, cursor)):
            cursor.execute('DELETE FROM Beneficiario WHERE id = ?', (id,))
            conexao.commit()
            conexao.close()
            return True
        else:
            return False
    finally:
        conexao.close() 
    
def buscar_beneficiario(id, cursor):
    cursor.execute('SELECT Usuario.id, Usuario.nome,Usuario.tipo, Usuario.cpf_cnpj, Usuario.tipo,' +
                    'Beneficiario.nome_beneficiario FROM Usuario  INNER JOIN Beneficiario ON Usuario.id = Beneficiario.id '+
                    'WHERE Usuario.id = ?', (id,))
    beneficiarios = cursor.fetchone()
    return beneficiarios