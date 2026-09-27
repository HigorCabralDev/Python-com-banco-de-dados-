import sqlite3

def conectar_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao

def cria_tabelas(conexao):
    cursor = conexao.cursor()

    cursor.execute (''' CREATE TABLE IF NOT EXISTS Locais
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Endereço TEXT NOT NULL) ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Eventos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Data TEXT NOT NULL,
    Local_id INTEGER NOT NULL,
    FOREIGN KEY (local_id) REFERENCES Locais (id))''')

    cursor.execute ('''CREATE TABLE IF NOT EXISTS Participantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    evento_id INTEGER NOT NULL,
    FOREIGN KEY (evento_id) REFERENCES Evento(id))''')

    conexao.commit()
    cursor.close() 
    
if __name__ == '__main__':
    conexao = conectar_banco('evento.db')
    cria_tabelas(conexao)
    conexao.close()