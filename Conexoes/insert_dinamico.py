import sqlite3 as conector 
from modelo import Pessoa

conexao = conector.connect("meu_banco.db")
cursor = conexao.cursor()

# Criação de um objeto do tipo Pessoa
pessoa = Pessoa (10000000009, 'MARIA', '1990-01-31', False)

# Definição de um comando com query parameter
comando = '''INSERT INTO Pessoa(Cpf, Nome, Nascimento, oculos)
VALUES (?, ?, ?, ?);'''

cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.data_nascimento, pessoa.usa_oculos))

conexao.commit()

cursor.close()
conexao.close()