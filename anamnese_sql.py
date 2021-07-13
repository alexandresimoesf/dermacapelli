import csv
from collections import deque
from itertools import islice
import time

medicos: dict = {'20': '203',
                 '25': '210',
                 '26': '212',
                 '2': '211'}


def anamnese(*args):
    with open('HISTORIC_NOVO.csv', 'r', newline='\n', encoding='latin-1') as file:
        reader = deque(csv.DictReader(file, delimiter=';'))
        sql_inicio = 'INSERT INTO public.anamnese('
        colunas = 'anamnese, checksum, datacriacao, fk_responsavel_id, fk_prontuario_id) VALUES ('
        with open('anamnese_sql_completo.sql', 'w', encoding='utf-8') as sql:
            for n, codigo_agenda, data_agenda in args[0]:
                historic = ''
                # tempo = time.time()
                for index, linha in enumerate(reader):
                    if index >= n:
                        if linha['CodMedico'] in medicos.keys():
                            codigo, data = linha['CodPaciente'], '{}{}{}{}-{}{}-{}{}'.format(*linha['DataConsulta'])
                            if codigo == codigo_agenda and data == data_agenda:
                                # print(linha)
                                if linha['Historico'] != 'null':
                                    historic += linha['Historico'] + '. '
                                historic = historic.replace('<Crlf>', '')
                                historic = historic.replace('<CRLF>', '')
                                fk_medico_id = medicos[linha['CodMedico']]

                        if linha['CodPaciente'] > codigo_agenda:
                            break

                sqlconteudo = "'{}', null, '{} 08:00:00', {}," \
                              " (SELECT p.id from public.prontuario p where fk_paciente_id = (select id from paciente where id_paciente_dermacapelli = {} limit 1)));".format(historic,
                                                                                                    data,
                                                                                                    fk_medico_id,
                                                                                                    codigo)
                sql_final = '{}{}{}\n'.format(sql_inicio, colunas, sqlconteudo)
                sql.write(sql_final)
                # file.seek(0)
    file.close()
    sql.close()
