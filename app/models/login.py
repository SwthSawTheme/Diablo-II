class User():

    def __init__(self, login:str,password:str):
        self.login = login
        self.password = password

    def register(self):
        insert = """
        INSERT INTO Users (Login, password)
        VALUES (?,?)"""

        return insert, (self.login, self.password)

    def login(self):
        pass

    def getUsers(self):
        pass
        