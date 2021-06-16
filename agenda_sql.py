import csv

medicos: dict = {'20': '203',
                 'n': '210',
                 'nn': '212'}

with open('HISTORIC_NOVO.csv', 'r', newline='\n', encoding='latin-1') as file:
    reader = csv.DictReader(file, delimiter=';')
    sql = open('agenda_sql.sql', 'w', encoding='latin-1')
    sql_inicio = 'INSERT INTO public.agenda('
    colunas = 'data_agendada, data_agendada_timestamp, horario, descricao, etiqueta, ' \
              'status, status_consulta, confirm_consulta, codigo_saida, data_solicitacao,' \
              'tipo_atendimento, tipo_atendimento, is_encaixe, data_atendimento, data_finalizacao,' \
              'responsavel_finalizacao, paciente_online, fk_clinica_id, fk_medico_id,' \
              'fk_paciente_id, fk_especializacao_id, fk_forma_atendimento_id) VALUES ('
    for n, linha in enumerate(reader):
        if linha['CodMedico'] in medicos.keys():
            if linha['Atributo'].startswith('@c') and linha['CodPaciente'] != 'null':
                data_agendada = '{}{}{}{}/{}{}/{}{}'.format(*linha['DataConsulta'])
                data_agendada_timestamp = '{} {}'.format(data_agendada, '08:00:00')
                horario = '08:00'
                descricao = ''
                etiqueta = 'consulta'
                status = '1'
                status_consulta = 'AGUARDANDO'
                confirm_consulta = 'CONFIRMADO'
                codigo_saida = 'RETORNO'
                data_solicitacao = data_agendada
                tipo_atendimento = 'CONSULTA'
                is_encaixe = 'false'
                data_atendimento = data_agendada
                data_finalizacao = 'null'
                responsavel_recepcao = ''
                paciente_online = 'false'
                fk_clinica_id = '83'
                fk_medico_id = medicos[linha['CodMedico']]
                fk_paciente_id = linha['CodPaciente']
                fk_especializacao_id = ''
                fk_forma_atendimento_id = ''

                sqlconteudo = "'{}', '{}', '{}', '{}', '{}', '{}'," \
                              " '{}', '{}', '{}', '{}', '{}', '{}'," \
                              " '{}', '{}', '{}', '{}', '{}', '{}'," \
                              " '{}', '{}', '{}', '{}');".format(data_agendada,
                                                                 data_agendada_timestamp,
                                                                 horario, descricao,
                                                                 etiqueta, status,
                                                                 status_consulta,
                                                                 confirm_consulta,
                                                                 codigo_saida,
                                                                 data_solicitacao,
                                                                 tipo_atendimento,
                                                                 is_encaixe,
                                                                 data_atendimento,
                                                                 data_finalizacao,
                                                                 responsavel_recepcao,
                                                                 paciente_online,
                                                                 paciente_online,
                                                                 fk_clinica_id,
                                                                 fk_medico_id,
                                                                 fk_paciente_id,
                                                                 fk_especializacao_id,
                                                                 fk_forma_atendimento_id)

                sqlfinal = '{}{}{}\n'.format(sql_inicio, colunas, sqlconteudo)
                sql.write(sqlfinal)
                # if n >= 1000:
                #     sql.close()
                #     file.close()
                #     break
sql.close()
file.close()
