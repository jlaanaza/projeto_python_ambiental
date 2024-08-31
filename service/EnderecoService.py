# service/EnderecoService.py
from banco.DatabaseConnection import conectar_banco
import sqlite3

def listar_enderecos():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM Endereco')
    enderecos = cursor.fetchall()
    conexao.close()
    return enderecos

def obter_endereco(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM Endereco WHERE id = ?', (id,))
    endereco = cursor.fetchone()
    conexao.close()
    return endereco

def cadastrar_endereco(dados):
    logradouro = dados.get('logradouro')
    cidade = dados.get('cidade')
    estado = dados.get('estado')
    cep = dados.get('cep')

    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        cursor.execute('''
            INSERT INTO Endereco (logradouro, cidade, estado, cep)
            VALUES (?, ?, ?, ?)
        ''', (logradouro, cidade, estado, cep))
        conexao.commit()
        id = cursor.lastrowid
        return id # Retorna o ID do endereço recém-criado
    except sqlite3.IntegrityError as e:
        print(f"Erro ao inserir endereço: {e}")
        return None
    finally:
        conexao.close()

def atualizar_endereco(dados, id):
    logradouro = dados.get('logradouro')
    cidade = dados.get('cidade')
    estado = dados.get('estado')
    cep = dados.get('cep')

    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        cursor.execute('''
            UPDATE Endereco
            SET logradouro = ?, cidade = ?, estado = ?, cep = ?
            WHERE id = ?
        ''', (logradouro, cidade, estado, cep, id))
        conexao.commit()
        return cursor.rowcount > 0
    finally:
        conexao.close()

def deletar_endereco(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        cursor.execute('DELETE FROM Endereco WHERE id = ?', (id,))
        conexao.commit()
        return cursor.rowcount > 0
    finally:
        conexao.close()
