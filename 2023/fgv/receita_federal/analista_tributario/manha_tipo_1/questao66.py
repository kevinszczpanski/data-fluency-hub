def xxx(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print (xxx(90,15))