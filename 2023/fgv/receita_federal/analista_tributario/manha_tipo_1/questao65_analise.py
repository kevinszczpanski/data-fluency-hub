# Comentário: o código cria uma lista vazia chamada L e, em seguida, utiliza um loop for 
# para iterar no intervalo de 10 a 1 (exclusivo) com um passo de -2. 
# A cada iteração, o valor atual de x é adicionado à lista L usando o método append(). 
# Por fim, o código imprime uma fatia da lista L, especificamente os elementos nas posições 2 e 3.

# Cria uma lista vazia chamada L
L = []  

# Loop for que itera no intervalo de 10 a 1 (exclusivo) com um passo de -2
for x in range(10, 1, -2):
    # Adiciona o valor atual de x à lista L
    L.append(x)  

# Testando

print(L[2:4])

# Aprofundando
# Alterando elementos da lista

print("Lista original:", L)

# Cria uma sublista a partir da lista L, contendo os elementos nas posições 2 e 3, lembrando que 
# indexação em Python começa em 0, então L[2:4] retorna os elementos nas posições 2 e 3 (exclusivo).

sublista = L[2:4]

# Imprime a sublista criada, contendo os elementos nas posições 2 e 3 da lista original.

print("Sublista:", sublista)


# Modificando a sublista para tribuir o valor 99 à primeira posição da sublista.

sublista[0] = 99

# Imprime as sublistas.

print("Sublista modificada:", sublista)
print("Lista original após modificação da sublista:", L)
