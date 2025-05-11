import sqlite3
from database import *

table_user = """
    CREATE TABLE IF NOT EXISTS USERS (
    ID_User INTEGER PRIMARY KEY AUTOINCREMENT,
    Login VARCHAR(12) NOT NULL,
    Password VARCHAR(12) NOT NULL)"""

def initialize():
    try:
        conexao = sqlite3.connect("Data.db")
        cursor = conexao.cursor()
        cursor.execute(table_user)
        conexao.commit()
        print("Alteração feitas com sucesso!")
    except Exception as e:
        print(f"Error:{e}")
    finally:
        if conexao:
            conexao.close()
            print("Conexão fechada com sucesso!")

if __name__ == "__main__":
    initialize()