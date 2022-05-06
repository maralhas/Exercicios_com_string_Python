from dataclasses import replace
import os
from unittest import result
os.system('cls')

# e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

sequencia = []
c = []
p = []
f = []
digito = []
def verificador(cpf):
    resultado  = 0
    regresso = 10
    cpf = cpf.replace('-', '.')
    cpf = cpf.split('.')

    primeira_part = cpf[0]
    segunga_part = cpf[1]
    terceira_part = cpf[2]

    for i in range(len(primeira_part)):
        c.append(int(primeira_part[i]))
        c[i] = int(primeira_part[i]) * regresso
        regresso -= 1

    for i in range(len(segunga_part)):
        p.append(int(segunga_part[i]))
        p[i] = int(segunga_part[i]) * regresso
        regresso -= 1
    
    for i in range(len(terceira_part)):
        f.append(int(terceira_part[i]))
        f[i] = int(terceira_part[i]) * regresso
        regresso -= 1
    
    resultado = sum(c) + sum(p) + sum(f)
    resultado *= 10
    resultado %= 11
    
    if resultado == 10:
        resultado = 0
    
    primeiro_digito = resultado
    regresso = 11
    for i in range(len(primeira_part)):
        c.append(int(primeira_part[i]))
        c[i] = int(primeira_part[i]) * regresso
        regresso -= 1

    for i in range(len(segunga_part)):
        p.append(int(segunga_part[i]))
        p[i] = int(segunga_part[i]) * regresso
        regresso -= 1
    
    for i in range(len(terceira_part)):
        f.append(int(terceira_part[i]))
        f[i] = int(terceira_part[i]) * regresso
        regresso -= 1
    for i in range(len(digito) -1):
        digito.append(int(digito[i]))
        digito[i] = int(digito[i]) * regresso
        regresso -= 1

    resultado = sum(c) + sum(p) + sum(f) + sum(digito)
    resultado *= 10
    resultado %= 11
    segundo_digito = resultado

    digito = ''.join(digito)
    if digito == cpf[3]:
        print('É valido')

entrada_cpf = input('Digite o CPF: ')
verificador(entrada_cpf)