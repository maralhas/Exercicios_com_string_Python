import os
os.system('cls')

# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), 
# conte:
# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.

lista_de_vogais = [0, 0, 0, 0, 0, 0]
lista_de_elementos = ['A','E','I', 'O', 'U', 'Espaço em branco']

def contador_de_espaco_e_vogais(frase):
    caracteres_ordenados = sorted(frase)

    for caracter in caracteres_ordenados[0:]:
        if caracter == ' ':
            lista_de_vogais[5] += 1
        elif caracter == 'a' or caracter == 'á' or caracter == 'à' or caracter == 'ã' or caracter == 'â':
            lista_de_vogais[0] += 1
        elif caracter == 'e' or caracter == 'é' or caracter == 'è' or caracter == 'ê':
            lista_de_vogais[1] += 1
        elif caracter == 'i' or caracter == 'í' or caracter == 'ì' or caracter == 'î':
            lista_de_vogais[2] += 1
        elif caracter == 'o' or caracter == 'ó' or caracter == 'ò' or caracter == 'õ' or caracter == 'ô':
            lista_de_vogais[1] += 1
        elif caracter == 'u' or caracter == 'ú' or caracter == 'ù' or caracter == 'û':
            lista_de_vogais[1] += 1

    for i in range(len(lista_de_vogais)):
        print(f'{lista_de_elementos[i]}: {lista_de_vogais[i]}')


frase = input('Digite uma frase: ').lower()
contador_de_espaco_e_vogais(frase)