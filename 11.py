import os
os.system('cls')

palavra = 'DevPro'.upper()
erros = 0
print('Jogo da forca')
print('Descubra a palavra')
print('A palavra é')

for letra in palavra:
    print(f'_ ', end = '')

conjuto_letras_palavra = set(palavra)
conjuto_letras_digitadas = set()

while (not conjuto_letras_palavra.issubset(conjuto_letras_digitadas)) and erros < 7:
    print()
    print()
    letra_digitada = input('Digite uma letra: ').upper()
    conjuto_letras_digitadas.add(letra_digitada)
    if letra_digitada in conjuto_letras_palavra:
        for letra in palavra:
            if letra in conjuto_letras_digitadas:
                print(f'{letra} ', end='')
            else:
                print('_ ', end='')
    else:
        erros += 1
        print(f'Você Errou {erros} de 6. Tente de novo')
    print()
    print('Letras já digitadas: ', conjuto_letras_digitadas)

if erros < 7:
    print('Parabéns você ganhou')
else: 
    print('Infelismente você perdeu')