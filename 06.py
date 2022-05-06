import os
os.system('cls')

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def data_mes_extenso(data):
    data[1] = meses[int(data[1]) -1]
    data_com_mes_por_extenso = '/'.join(data)
    return print(data_com_mes_por_extenso)

data = input('Digite a data no dormato dd/mm/aaaa: ').split('/')
data_mes_extenso(data)