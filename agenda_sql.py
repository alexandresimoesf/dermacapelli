import csv
from anamnese_sql import anamnese

medicos: dict = {'20': '203',
                 '25': '210',
                 '26': '212',
                 '2': '211'}

especializacao = {'203': '776',
                  '210': '798',
                  '213': '806',
                  '212': '804',
                  '214': '808',
                  '211': '801'}

agenda_to_anamnese: list = []
prontuario_ja_criado = []
permissao_prontuario_clinico = []

with open('HISTORIC_NOVO.csv', 'r', newline='\n', encoding='latin-1') as file:
    reader = csv.DictReader(file, delimiter=';')
    sql = open('agenda_sql_completo.sql', 'w', encoding='latin-1')
    sql_inicio_agenda = 'INSERT INTO public.agenda('
    colunas_agenda = 'data_agendada, data_agendada_timestamp, horario, descricao, etiqueta, ' \
              'status, status_consulta, confirm_consulta, codigo_saida, data_solicitacao,' \
              'tipo_atendimento, is_encaixe, data_atendimento, data_finalizacao,' \
              'paciente_online, fk_clinica_id, fk_medico_id,' \
              'fk_paciente_id, fk_especializacao_id, fk_forma_atendimento_id) VALUES ('
    for n, linha in enumerate(reader):
        if linha['CodMedico'] in medicos.keys():
            if linha['Atributo'].startswith('@c') and linha['CodPaciente'] != 'null':
                data_agendada = '{}{}{}{}-{}{}-{}{}'.format(*linha['DataConsulta'])
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
                fk_especializacao_id = especializacao[fk_medico_id]
                fk_forma_atendimento_id = '230'

                sql_conteudo_agenda = "'{}', '{}', '{}', '{}', '{}', {}," \
                                      " '{}', '{}', '{}', '{}', '{}', {}," \
                                      " '{}', {}, {}, {}, {}," \
                                      " (SELECT id FROM public.paciente where paciente.id_paciente_dermacapelli = {}), {}, {});".format(data_agendada,
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
                                                                                                                                        paciente_online,
                                                                                                                                        fk_clinica_id,
                                                                                                                                        fk_medico_id,
                                                                                                                                        fk_paciente_id,
                                                                                                                                        fk_especializacao_id,
                                                                                                                                        fk_forma_atendimento_id)

                sqlfinal = '{}{}{}\n'.format(sql_inicio_agenda, colunas_agenda, sql_conteudo_agenda)
                sql.write(sqlfinal)

                if fk_paciente_id in prontuario_ja_criado:
                    pass
                else:
                    prontuario_ja_criado.append(fk_paciente_id)
                    sql.write('INSERT INTO public.prontuario(datacriacao, fk_paciente_id) SELECT now(), id from public.paciente where paciente.id_paciente_dermacapelli = {};\n'.format(
                        fk_paciente_id))
                    sql.write('INSERT INTO public.permissao_prontuario_clinica(modificado_em, fk_medico_id, fk_prontuario_id, fk_rede_clinica_id, escrita, leitura)'
                              ' VALUES'
                              ' (now(), {},'
                              ' (SELECT id FROM public.prontuario WHERE fk_paciente_id = (SELECT id FROM paciente where paciente.id_paciente_dermacapelli={} LIMIT 1)),'
                              ' (SELECT fk_rede_clinica_id FROM public.clinica WHERE id = (83)), false, false);\n'.format(fk_medico_id, fk_paciente_id))

                agenda_to_anamnese.append((n, linha['CodPaciente'], data_agendada))
                # if linha['CodPaciente'] == '3215':
                #     sql.close()
                #     file.close()
                #     anamnese(agenda_to_anamnese)
                #     break
sql.close()
file.close()
# anamnese(agenda_to_anamnese)
