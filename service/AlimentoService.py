# service/AlimentoService.py
from banco.DatabaseConnection import conectar_banco
from service.EnderecoService import cadastrar_endereco

import sqlite3

def listar_alimentos():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT Alimento.nome, Alimento.quantidade, Alimento.perecivel, Alimento.data_validade,
               Colaborador.nome_colaborador, Endereco.logradouro, Endereco.cidade, Endereco.estado, Endereco.cep,
               Usuario.nome
        FROM Alimento
        INNER JOIN Colaborador ON Alimento.colaborador_id = Colaborador.id
        INNER JOIN Usuario ON Usuario.id = Colaborador.id 
        INNER JOIN Endereco ON Alimento.endereco_id = Endereco.id
    ''')
    alimentos = cursor.fetchall()
    conexao.close()
    return alimentos

def obter_alimento(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT Alimento.nome, Alimento.quantidade, Alimento.perecivel, Alimento.data_validade,
               Colaborador.nome_colaborador, Endereco.logradouro, Endereco.cidade, Endereco.estado, Endereco.cep,
               Usuario.nome
        FROM Alimento
        INNER JOIN Colaborador ON Alimento.colaborador_id = Colaborador.id
        INNER JOIN Usuario ON Usuario.id = Colaborador.id           
        INNER JOIN Endereco ON Alimento.endereco_id = Endereco.id
        WHERE Alimento.id = ?
    ''', (id,))
    alimento = cursor.fetchone()
    conexao.close()
    return alimento


def cadastrar_alimento(dados):
    nome = dados.get('nome')
    quantidade = dados.get('quantidade')
    perecivel = dados.get('perecivel')
    data_validade = dados.get('data_validade')
    colaborador_id = dados.get('colaborador_id')
    endereco_dados = dados.get('endereco')

    if not verificar_colaborador(colaborador_id):
        return False, "Colaborador não encontrado."
    
    endereco_id = cadastrar_endereco(endereco_dados)
    if not verificar_endereco(endereco_id):
        return False, "Endereço não encontrado."

    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        cursor.execute('''
        INSERT INTO Alimento (nome, quantidade, perecivel, data_validade, colaborador_id, endereco_id)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (nome, quantidade, perecivel, data_validade, colaborador_id, endereco_id))
        conexao.commit()
        return True, "Alimento criado com sucesso!"
    except sqlite3.IntegrityError:
        return False, "Erro ao criar alimento."
    finally:
        conexao.close()

def atualizar_alimento(dados, id):
    nome = dados.get('nome')
    quantidade = dados.get('quantidade')
    perecivel = dados.get('perecivel')
    data_validade = dados.get('data_validade')
    colaborador_id = dados.get('colaborador_id')
    endereco_dados = dados.get('endereco')

    if not verificar_colaborador(colaborador_id):
        return False, "Colaborador não encontrado."
    
    endereco_id = cadastrar_endereco(endereco_dados)
    if not verificar_endereco(endereco_id):
        return False, "Endereço não encontrado."

    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        cursor.execute('''
            UPDATE Alimento
            SET nome = ?, quantidade = ?, perecivel = ?, data_validade = ?, colaborador_id = ?, endereco_id = ?
            WHERE id = ?
        ''', (nome, quantidade, perecivel, data_validade, colaborador_id, endereco_id, id))
        conexao.commit()
        return cursor.rowcount > 0, "Atualizado com sucesso"
    except sqlite3.DatabaseError:
        return False, "Ocorreu um erro"
    finally:
        conexao.close()

def deletar_alimento(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        cursor.execute('DELETE FROM Alimento WHERE id = ?', (id,))
        conexao.commit()
        return cursor.rowcount > 0
    finally:
        conexao.close()

def verificar_colaborador(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT id FROM Colaborador WHERE id = ?', (id,))
    existe = cursor.fetchone() is not None
    conexao.close()
    return existe

def verificar_endereco(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT id FROM Endereco WHERE id = ?', (id,))
    existe = cursor.fetchone() is not None
    conexao.close()
    return existe
