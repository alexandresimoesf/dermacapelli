import time
import csv
from collections import deque

pacientes = deque(['', ''], maxlen=2)


def meu_arquivo():
    with open('HISTORIC_NOVO.csv', 'r', encoding='latin-1') as documento:
        leitura = csv.DictReader(documento, delimiter=';')
        for index, linha in enumerate(leitura):
            yield index, linha


arquivo = meu_arquivo()
for i in range(3):
    print(str(i) + ' Loop')
    while True:
        um = next(arquivo)
        dois = next(arquivo)
        pacientes.append(um[1]['CodPaciente'])
        pacientes.append(dois[1]['CodPaciente'])
        if um[1]['CodPaciente'] != dois[1]['CodPaciente']:
            print(um[1]['CodPaciente'], dois[1]['CodPaciente'])
            print(pacientes)
            break


# for i in range(3):
#     print('Estou no loop {}'.format(i))
#     um = next(arquivo)
#     dois = next(arquivo)
#     pacientes.append(um[1])
#     pacientes.append(dois[1])
#     print(pacientes)