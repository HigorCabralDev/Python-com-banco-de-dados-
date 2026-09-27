import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("meu_banco.db")
cursor = conexao.cursor()

# Execução de um comando: SELECT... CREATE ...

comando1 = '''DROP TABLE Veiculo'''

cursor.execute(comando1)

# Efetivação do comando 

conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()

