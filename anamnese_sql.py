import csv

medicos: dict = {'20': '203',
                 'n25': '210',
                 'n26': '212',
                 'n2': '211'}


def anamnese(*args):
    with open('HISTORIC_NOVO.csv', 'r', newline='\n', encoding='latin-1') as file:
        reader = csv.DictReader(file, delimiter=';')
        sql_inicio = 'INSERT INTO public.anamnese('
        colunas = '(anamnese, checksum, datacriacao, fk_responsavel_id, fk_prontuario_id) VALUES ('

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
                historic = historic.replace('<Crlf>', '').replace('<CRLF>', '')
                print(linha['CodMedico'])
                # fk_medico_id = medicos[linha['CodMedico']]
                sqlconteudo = "'{}', null, '{} 08:00:00', '{}', 'valor sql');".format(historic, data, linha['CodMedico'])
                sql_final = '{}{}{}\n'.format(sql_inicio, colunas, sqlconteudo)
                sql.write(sql_final)
                file.seek(0)
    # file.close()
    # sql.close()
