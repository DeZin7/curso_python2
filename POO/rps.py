# Pedra, papel e tesoura é um jogo com dois participantes. O jogo tem rodadas. 
# Em cada rodada, um participante escolhe um símbolo de pedra, papel ou tesoura, e o outro participante faz o mesmo. 
# O vencedor da rodada é determinado pela comparação dos símbolos escolhidos. 
# As regras do jogo estabelecem que pedra ganha de tesoura, tesoura vence (corta) papel e papel vence (embrulha) pedra. 
# O vencedor da rodada recebe um ponto. 
# O jogo continua pela quantidade de rodadas que os participantes combinarem. 
# O vencedor é o participante com o maior número de pontos

class Participante:
    def __init__(self, name):
        self.name = name
        self.pontos = 0
        self.simbolo = ""
        

    def choose(self):
        self.simbolo = input(f'{self.name} selecione pedra, papel ou tesoura: ')
        print(f'{self.name} escolheu {self.simbolo}')



class GameRound:
    def __init__(self, p1, p2):
        p1.choose()
        p2.choose()
    
    def compare(self):
        print('Implement')

    def awardpoints(self):
        print('Implement')


class Game:
    def __init__(self):
        self.endgame = False
        self.participante = Participante("deca")
        self.secondParticipante = Participante("durateston")

    def start(self):
        game_round = GameRound(self.participante, self.secondParticipante)

    def check_condition(self):
        print('Implement')
    
    def winner(self):
        print('Implement')




game = Game()
game.start()
