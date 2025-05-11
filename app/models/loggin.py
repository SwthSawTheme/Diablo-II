class User():

    def __init__(self, login:str,password:str):
        self.login = login
        self.password = password

    def register(self, login: str, password:str):
        insert = """
        INSERT INTO User (Login, password)
        VALUES (?,?)"""

        return insert, (login, password)

    def login(self):
        pass

    def getUsers(self):
        pass
        