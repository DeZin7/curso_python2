# method vs @classmethod vc @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe. ele recebe a classe como parâmetro
# @staticmethod - método estático (não recebe self nem cls)

# qualquer método no qual eu use self, esse método é um método de instância (instância é o objeto)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_authentication(cls, user, password):
        connection = cls
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def soma(x, y):
        return x + y


c1 = Connection()
# c1.set_user('Dezin')
# c1.set_password('123')
c1 = Connection.create_with_authentication('Dezin', '123')
print(c1.user)
print(c1.password)
print(Connection.soma(1, 3))