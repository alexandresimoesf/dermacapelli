import csv


def anamnese(*args):
    with open('HISTORIC_NOVO.csv', 'r', newline='\n', encoding='latin-1') as file:
        reader = csv.DictReader(file, delimiter=';')
        sql = open('anamnese_sql.sql', 'w', encoding='latin-1')
        for codigo_agenda, data_agenda in args[0]:
            # print('#' * 10)
            # print(codigo_agenda, data_agenda)
            for linha in reader:
                codigo, data = linha['CodPaciente'], '{}{}{}{}/{}{}/{}{}'.format(*linha['DataConsulta'])
                if codigo == codigo_agenda and data == data_agenda:
                    if linha['Historico'] != 'null':
                        sql.write('{}. '.format(linha['Historico'].title()))
            file.seek(0)
    file.close()
    sql.close()
