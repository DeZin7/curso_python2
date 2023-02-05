# raise - lançando excessões

def divide(n, d):
    if d == 0:
        raise ZeroDivisionError('Vc está tentando dividir por zero.')

    return n / d

# print(divide(8, 0))

import sys

print(sys.platform)
