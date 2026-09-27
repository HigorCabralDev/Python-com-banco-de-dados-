import sqlite3 as conector
from modelo import Pessoa

conexao = conector.connect("meu_banco.db")
cursor = conexao.cursor()

# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(20000000009, 'José', '1990-02-28', False)

# Definição de um comando com query parameter
comando = '''INSERT INTO Pessoa (Cpf, Nome, Nascimento, oculos)
VALUES (:cpf, :nome, :data_nascimento, :usa_oculos);'''

cursor.execute(comando,{"cpf": pessoa.cpf,
                         "nome": pessoa.nome,
                         "data_nascimento": pessoa.data_nascimento,
                         "usa_oculos": pessoa.usa_oculos})

conexao.commit()

cursor.close()
conexao.close()
