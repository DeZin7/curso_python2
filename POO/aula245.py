# Método especiasl __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma classe callable

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, *args, **kwargs):
        print(f'Chamando, {self.phone}...')

calldrogo = CallMe('805 906-0497')
calldrogo(123)