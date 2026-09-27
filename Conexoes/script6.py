import sqlite3 as conector 

conexao = conector.connect("meu_banco.db")
cursor = conexao.cursor()

comando = '''INSERT INTO Pessoa (Cpf,Nome, Nascimento, oculos)
VALUES (12345678900, 'João', '2004-12-26', 1)'''

cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()