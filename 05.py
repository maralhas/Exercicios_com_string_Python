import os
os.system('cls')

nome = input('Digite um nome: ').upper()
i = len(nome) + 1
for letra in nome:
    i -= 1
    print (nome[:i])