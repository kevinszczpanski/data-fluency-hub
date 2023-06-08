# Comentário: a função xxx(a, b) implementa o algoritmo de Euclides para encontrar o máximo divisor comum (MDC) entre dois números inteiros a e b.

def xxx(a, b):
    """
    Calcula o máximo divisor comum (MDC) entre dois números inteiros.

    Parâmetros:
    a (int): O primeiro número.
    b (int): O segundo número.

    Retorna:
    int: O máximo divisor comum entre os números a e b.

    """

    while b != 0:
        a, b = b, a % b

    return a

# Testando

print(xxx(90, 15))

print(xxx(120,23))

# Aprodundando:  vamos criar outra função para implementar o algoritmo de Euclides estendido, que também calcula o máximo divisor comum (MDC), mas também retorna os coeficientes de Bézout, que são os números inteiros x e y que satisfazem a equação ax + by = MDC(a, b).

def euclides_estendido(a, b):
    """
    Calcula o máximo divisor comum (MDC) entre dois números inteiros utilizando o algoritmo de Euclides estendido.

    Parâmetros:
    a (int): O primeiro número.
    b (int): O segundo número.

    Retorna:
    tuple: Uma tupla contendo o MDC(a, b) e os coeficientes de Bézout (x, y) na forma (MDC, x, y).

    """

    if b == 0:
        return a, 1, 0

    mdc, x1, y1 = euclides_estendido(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return mdc, x, y

# Testando

mdc, x, y = euclides_estendido(90, 15)
print("MDC:", mdc)
print("Coeficientes de Bézout (x, y):", x, y)
print(f"Equação completa: 90 * {x} + 15 * {y} = {mdc}")

mdc, x, y = euclides_estendido(120, 23)
print("MDC:", mdc)
print("Coeficientes de Bézout (x, y):", x, y)
print(f"Equação completa: 120 * {x} + 23 * {y} = {mdc}")

