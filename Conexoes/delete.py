import sqlite3 as conector

conexao = conector.connect("meu_banco.db")
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

# Definição dos comandos 
comando  = '''DELETE FROM Pessoa WHERE cpf = 200000000009; '''
cursor.execute (comando)

comando2 = '''DELETE FROM Pessoa WHERE cpf = 200000000099;'''

cursor.execute (comando2)
conexao.commit()

cursor.close()
conexao.close()