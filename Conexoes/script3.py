import sqlite3 as conector 

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("meu_banco.db")
cursor = conexao.cursor()

# Execução de um comando: SELECT... CREATE ...
comando = '''CREATE TABLE Veiculo(
Placa CHARACTER (7) NOT NULL,
Ano INTEGER NOT NULL,
Cor TEXT NOTL NULL,
Proprietario INTEGER NOT NULL,
Marca INTEGER NOT NULL,
PRIMARY KEY (Placa),
FOREIGN KEY(Proprietario) REFERENCES Pessoa(cpf),
FOREIGN KEY(Marca) REFERENCES Marca(id));'''

cursor.execute(comando)

# Efetivação do comando 
conexao.commit()

# Fechamento das conexões 
cursor.close()
conexao.close()