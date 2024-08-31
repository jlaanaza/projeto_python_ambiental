import sqlite3
from banco.DatabaseConnection import conectar_banco


def listar_usuarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM Usuario')
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

def obter_usuario(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    usuarios = buscar_usuario(id, cursor)
    conexao.close()
    return usuarios

def cadastrar_usuario(dados):
    nome = dados.get('nome')
    cpf_cnpj = dados.get('cpf_cnpj')
    senha = dados.get('senha')    
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        cursor.execute('INSERT INTO Usuario (nome, cpf_cnpj, tipo, senha) VALUES (?, ?, ?, ?)', (nome, cpf_cnpj, 'colaborador', senha))
        conexao.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
    return cursor.lastrowid

def atualizar_usuario(dados, id):
    nome = dados.get('nome')
    cpf_cnpj = dados.get('cpf_cnpj')
    tipo = dados.get('tipo')
    senha = dados.get('senha')

    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        if(buscar_usuario(id, cursor)):       
            cursor.execute('UPDATE Usuario SET nome = ?, cpf_cnpj = ?, tipo = ?, senha = ? WHERE id = ?', (nome, cpf_cnpj, tipo, senha, id))
            conexao.commit()
            return True
        else :
            return False
    finally:
        conexao.close()
    
def deletar_usuario(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        if(buscar_usuario(id, cursor)):
            cursor.execute('DELETE FROM Usuario WHERE id = ?', (id,))
            conexao.commit()
            conexao.close()
            return True
        else:
            return False
    finally:
        conexao.close()
    
def buscar_usuario(id, cursor):
    cursor.execute('SELECT * FROM Usuario WHERE id = ?', (id,))
    usuarios = cursor.fetchone()
    return usuarios
    