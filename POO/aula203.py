# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando, irmão.')
            return #com isso eu paro a função

        print(f'{self.nome} está filmando.')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return
        print(f'{self.nome} está fotografando')
    
    def parar_de_filmar(self):
        if self.filmando is not True:
            print(f'{self.nome} não está filmando')
            return
        print(f'{self.nome} está parando de filmar')
        self.filmando = False


c1 = Camera('Canon')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_de_filmar()
c1.fotografar()

