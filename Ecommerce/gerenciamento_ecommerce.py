import sqlite3

def conectar_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao

def criar_tabelas(conexao):
    cursor = conexao.cursor()

    cursor.execute (''' CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXTE NOT NULL,
    Preco REAL NOT NULL,
    Estoque INTEGER NOT NULL)''')

    cursor.execute ('''CREATE TABLE IF NOT EXISTS Clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL)''')

    cursor.execute ('''CREATE TABLE IF NOT EXISTS Pedidos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Cliente_id INTEGER NOT NULL,
    Produto_id INTEGER NOT NULL,
    Quantidade INTEGER NOT NULL,
    Data_pedido TEXT NOT NULL,
    FOREIGN KEY (Cliente_id) REFERENCES Clientes(id),
    FOREIGN KEY (Produto_id) REFERENCES Produtos(id)) ''')

    conexao.commit()
    cursor.close()

def inserir_dados(conexao):
    cursor = conexao.cursor()

    produtos = [('Notebook', 2999.99, 10),
                    ('Smartphone',1999.99,10),
                    ('Tablet', 999.90,30)]

    clientes = [('Alice', 'alice@exemple.com'),
                    ('Bob', 'bob@example.com'),
                    ('Chalie', 'chalie@example.com')]

    pedidos = [(1, 1, 2, '2023-06-15'),
                   (2, 2, 1, '2023-06-16'),
                   (3, 3, 3, '2023-06-17')]

    cursor.executemany('INSERT INTO Produtos (Nome, Preco, Estoque) VALUES (?, ?, ?)',
                           produtos)

    cursor.executemany('INSERT INTO Clientes (Nome, Email) VALUES (?, ?)',clientes)

    cursor.executemany ('INSERT INTO Pedidos (Cliente_id, Produto_id, Quantidade, Data_pedido) VALUES (?, ?, ?, ?)', pedidos)

    conexao.commit()
    cursor.close()

if __name__ == '__main__':
    conexao = conectar_banco('ecommerce.db')
    criar_tabelas(conexao)
    inserir_dados(conexao)
    conexao.close()