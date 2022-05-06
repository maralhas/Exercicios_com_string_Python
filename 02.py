import os
os.system('cls')

nome = input('Digite o nome: ').upper()

nome_invertido_por_letras = ''.join(reversed(nome))
nome_invertido_por_palavras = ' '.join(reversed(nome.split()))

print(f'Nome com letras em maiuscula: {nome}')
print(f'Nome com letras em maiuscolas invertido por letras {nome_invertido_por_letras}')
print(f'Nome com letras em maiuscolas invertido por palabras {nome_invertido_por_palavras}')
