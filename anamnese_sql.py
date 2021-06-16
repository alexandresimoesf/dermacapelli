import csv
from collections import defaultdict


def anamnese(*args):
    with open('HISTORIC_NOVO.csv', 'r', newline='\n', encoding='latin-1') as file:
        reader = csv.DictReader(file, delimiter=';')
        for i in reader:
            if i['CodPaciente'] == str(args[0][0][0]):
                print(i)
                break
        # linha = next(reader)

        # codigo , data = linha['CodPaciente'], '{}{}{}{}/{}{}/{}{}'.format(*linha['DataConsulta'])
        #
        # for id, data_agenda in args[0]:
        #     print(id, data_agenda)
        #     print(codigo, data)
        #     print('#' * 10)
        file.close()
        exit()