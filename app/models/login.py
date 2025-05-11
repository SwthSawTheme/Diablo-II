import sqlite3

class User():

    def __init__(self, login:str,password:str):
        self.login = login
        self.password = password

    def register(self):
        insert = """
        INSERT INTO Users (Login, password)
        VALUES (?,?)"""

        return insert, (self.login, self.password)

    def logar(self):
        try:
            conexao = sqlite3.connect("Data.db")
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM USERS WHERE Login = ? AND password = ?",(self.login,self.password))
            if cursor.fetchone():
                print("Logado com sucesso!")
            else:
                print("Login ou senha incorretos!")
        except Exception as e:
            print(f"Error{e}")


    def getUsers(self):
        pass

if __name__ == "__main__":
    user = str(input("Usuario: "))
    password = str(input("Senha: "))
    usuario = User(user,password)
    usuario.logar()