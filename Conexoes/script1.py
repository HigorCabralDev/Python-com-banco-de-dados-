import sqlite3 as conector

try:
    conexao = conector.connect('/meu_banco.db')
    cursor = conexao.cursor()

    comando = """
    CREATE TABLE IF NOT EXISTS Pessoa (
        cpf INTEGER NOT NULL,
        nome TEXT NOT NULL,
        nascimento DATE NOT NULL,
        oculos BOOLEAN NOT NULL,
        PRIMARY KEY (cpf)
    );
    """

    cursor.execute(comando)
    conexao.commit()

    print("Tabela criada com sucesso!")

except conector.DatabaseError as err:
    print("Erro de banco de dados:", err)

finally:
    if 'conexao' in locals():
        cursor.close()
        conexao.close()