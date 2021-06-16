import csv
from itertools import starmap

def anamnese(*args):
    with open('HISTORIC_NOVO.csv', 'r', newline='\n', encoding='latin-1') as file:
        reader = iter(csv.DictReader(file, delimiter=';'))
        linha = next(reader)
        codigo, data = linha['CodPaciente'], '{}{}{}{}/{}{}/{}{}'.format(*linha['DataConsulta'])
        for id, data_agenda in args[0]:
            print(id, data_agenda)
            print(codigo, data)
            print('#' * 10)
            break
        file.close()
        exit()