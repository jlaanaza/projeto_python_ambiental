from banco.DatabaseConnection import conectar_banco
from service.UsuarioService import cadastrar_usuario

def listar_colaboradores():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT Usuario.id, Usuario.nome,Usuario.tipo, Usuario.cpf_cnpj, Usuario.tipo,' +
                    'Colaborador.nome_colaborador FROM Usuario  INNER JOIN Colaborador ON Usuario.id = Colaborador.id')
    colaboradores = cursor.fetchall()
    conexao.close()
    return colaboradores

def obter_colaborador(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    colaboradores = buscar_colaborador(id, cursor)
    conexao.close()
    return colaboradores

def cadastrar_colaborador(dados):
    nome_colaborador = dados.get('nome_colaborador')  # Nome social ou pseudônimo

    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Criar o usuário primeiro
    usuario_id = cadastrar_usuario(dados)  # Obter o ID gerado para o usuário
    try:
        if(usuario_id):
            # Criar o colaborador com o ID do usuário recém-criado
            cursor.execute('INSERT INTO Colaborador (id, nome_colaborador) VALUES (?, ?)', (usuario_id, nome_colaborador))
            conexao.commit()
            return True
        else:
            return False
    finally:
        conexao.close()    

def atualizar_colaborador(dados, id):
    nome = dados.get('nome')
    cpf_cnpj = dados.get('cpf_cnpj')
    tipo = dados.get('tipo')
    senha = dados.get('senha')
    nome_colaborador = dados.get('nome_colaborador')

    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        if(buscar_colaborador(id, cursor)):       
            cursor.execute('UPDATE Usuario SET nome = ?, cpf_cnpj = ?, tipo = ?, senha = ? WHERE id = ?', (nome, cpf_cnpj, tipo, senha, id))
            cursor.execute('UPDATE Colaborador SET nome_colaborador = ? WHERE id = ?', (nome_colaborador, id))
            conexao.commit()
            conexao.close()
            return True
        else :
            return False
    finally:
        conexao.close() 
    
def deletar_colaborador(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        if(buscar_colaborador(id, cursor)):
            cursor.execute('DELETE FROM Colaborador WHERE id = ?', (id,))
            conexao.commit()
            conexao.close()
            return True
        else:
            return False
    finally:
        conexao.close() 
    
def buscar_colaborador(id, cursor):
    cursor.execute('SELECT Usuario.id, Usuario.nome,Usuario.tipo, Usuario.cpf_cnpj, Usuario.tipo,' +
                    'Colaborador.nome_colaborador FROM Usuario  INNER JOIN Colaborador ON Usuario.id = Colaborador.id '+
                    'WHERE Usuario.id = ?', (id,))
    colaboradores = cursor.fetchone()
    return colaboradores