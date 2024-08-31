import sqlite3

def conectar_banco():
    return sqlite3.connect('empresa.db')

def inicializar_banco():

    conn = conectar_banco()
    # Conectar ao banco de dados (ou criar se não existir)    
    cursor = conn.cursor()

    # Criar tabela Usuário
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf_cnpj TEXT UNIQUE NOT NULL,
        tipo TEXT NOT NULL,
        senha TEXT NOT NULL
    )
    ''')

    # Criar tabela Colaborador
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Colaborador (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_colaborador TEXT,
        FOREIGN KEY(usuario_id) REFERENCES Usuario(id) ON DELETE CASCADE
    )
    ''')

    # Criar tabela Beneficiário
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Beneficiario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_beneficiario TEXT,
        FOREIGN KEY(usuario_id) REFERENCES Usuario(id) ON DELETE CASCADE
    )
    ''')

    # Criar tabela Alimento
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Alimento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        perecivel BOOLEAN NOT NULL,
        data_validade DATE,
        colaborador_id INTEGER,
        endereco_id INTEGER,
        FOREIGN KEY(colaborador_id) REFERENCES Colaborador(id),
        FOREIGN KEY(endereco_id) REFERENCES Endereco(id)
    )
    ''')

    # Criar tabela Endereço
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Endereco (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        logradouro TEXT NOT NULL,
        cidade TEXT NOT NULL,
        estado TEXT NOT NULL,
        cep TEXT NOT NULL
    )
    ''')

    # Criar tabela Tabela Nutricional
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS TabelaNutricional (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        alimento_id INTEGER,
        ferro INTEGER,
        zinco INTEGER,
        minerais TEXT,
        beneficios TEXT,
        FOREIGN KEY(alimento_id) REFERENCES Alimento(id)
    )
    ''')

    # Confirmar as mudanças
    conn.commit()

    # Fechar a conexão
    conn.close()