import csv
from itertools import starmap


def anamnese(*args):
    with open('HISTORIC_NOVO.csv', 'r', newline='\n', encoding='latin-1') as file:
        reader = csv.DictReader(file, delimiter=';')
        # reader = list(reader.items())
        # linha = next(reader)
        for i in reader:
            print(list(i.items()))
            break
        # codigo , data = linha['CodPaciente'], '{}{}{}{}/{}{}/{}{}'.format(*linha['DataConsulta'])
        #
        # for id, data_agenda in args[0]:
        #     print(id, data_agenda)
        #     print(codigo, data)
        #     print('#' * 10)
        file.close()
        exit()