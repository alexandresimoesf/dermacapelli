import csv


def anamnese(*args):
    with open('HISTORIC_NOVO.csv', 'r', newline='\n', encoding='latin-1') as file:
        reader = csv.DictReader(file, delimiter=';')
        for codigo_agenda, data_agenda in args[0]:
            print('#' * 10)
            print(codigo_agenda, data_agenda)
            for linha in reader:
                codigo, data = linha['CodPaciente'], '{}{}{}{}/{}{}/{}{}'.format(*linha['DataConsulta'])
                if codigo == codigo_agenda and data == data_agenda:
                    if linha['Historico'] != 'null':
                        print(linha['Historico'])
        file.close()
        exit()
