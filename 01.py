import os
os.system('cls')

string_1 = input('Digite uma palavra: ')
string_2 = input('Digite outa palavra: ')

tamanho_string_1 = len(string_1)
tamanho_string_2 = len(string_2)

print(f'"{string_1}": {tamanho_string_1} caracteres')
print(f'"{string_2}": {tamanho_string_2} caracteres')

comparacao_de_tamalho = 'diferentes'
comparacao_de_conteudo = 'diferente'

if string_1 == string_1:
    comparacao_de_tamalho = 'iguais'
    comparacao_de_conteudo = 'igual'
elif tamanho_string_1 == tamanho_string_2:
    comparacao_de_tamalho = 'igual'

print(f'As duas strings são de tamanhos {comparacao_de_tamalho}.')
print(f'As duas strings possuem conteúdo {comparacao_de_conteudo}.')