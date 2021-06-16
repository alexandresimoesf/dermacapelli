import csv


def anamnese(*args):
    with open('HISTORIC_NOVO.csv', 'r', newline='\n', encoding='latin-1') as file:
        reader = csv.DictReader(file, delimiter=';')
        with open('anamnese_sql.sql', 'w', encoding='utf-8') as sql:
            for codigo_agenda, data_agenda in args[0]:
                historic = ''
                print('#' * 10)
                print(codigo_agenda, data_agenda)
                for linha in reader:
                    codigo, data = linha['CodPaciente'], '{}{}{}{}/{}{}/{}{}'.format(*linha['DataConsulta'])
                    if codigo == codigo_agenda and data == data_agenda:
                        if linha['Historico'] != 'null':
                            historic += linha['Historico'] + '. '
                historic = historic.replace('<Crlf>', '')
                historic = historic.replace('<CRLF>', '')
                sql.write(historic+'\n')
                file.seek(0)
    # file.close()
    # sql.close()
