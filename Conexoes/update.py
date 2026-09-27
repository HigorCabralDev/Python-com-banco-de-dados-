import sqlite3 as concector

conexao = concector.connect("meu_banco.db")
conexao.execute ("PRAGMA foreign_kayes = on")
cursor = conexao.cursor()

# Definição de comandos
comando1 = '''UPDATE Pessoa SET oculos = 1;'''
cursor.execute (comando1)
conexao.commit()

comando2 = '''UPDATE Pessoa SET oculos = ? WHERE cpf=20000000009;'''
cursor.execute(comando2, (False,))

comando3 = '''UPDATE Pessoa SET oculos= :usa_oculos WHERE cpf=:cpf;'''
cursor. execute (comando3, {"usa_oculos": False, "cpf":20000000009})

conexao.commit()

cursor.close()
conexao.close()