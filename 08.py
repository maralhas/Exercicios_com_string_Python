import os
os.system('cls')

# Palíndromo. 
# Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. 
# Por exemplo: OSSO e OVO são palíndromos. 
# Em textos mais complexos os espaços e pontuação são ignorados. 
# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. 
# Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

def palindromo(frase):
    frase = ''.join(frase)
    palindromo = ''.join(frase[::-1])

    if palindromo == frase:
        return print(f'{palindromo} é um palindromo')
    else:
        return print(f'{palindromo} não é um palindromo')

frase = input('Digite uma frase: ').upper().split(' ')
palindromo(frase)