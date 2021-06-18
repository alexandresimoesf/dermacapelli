import pandas as pd
import csv

#
# paciente = pd.read_csv('PACIENTE_NOVO.csv', sep=';', low_memory=False, encoding='latin-1')
# print(paciente.shape)
# print('#'*10)
# agenda = pd.read_csv('HISTORIC_NOVO.csv', sep=';', low_memory=False, encoding='latin-1')
# print(agenda.shape)
# print('#'*10)

# combinar = pd.merge(paciente, agenda, left_on='CodPaciente', right_on='CodPaciente', how='inner')
# print(combinar.shape)
# # combinar = combinar.add_suffix('\"').add_prefix('\"')
# combinar.to_csv('combinacao.csv', sep=';', escapechar='\\', quoting=csv.QUOTE_ALL, index=False, encoding='latin-1')
# print('#'*10)
#
# combinacao = pd.read_csv('combinacao.csv', sep=';', encoding='latin-1', dtype='unicode')
# print(combinacao.shape)
# combinacao["CodMedico_x"] = combinacao["CodMedico_x"].astype(str)
# medicos = pd.read_csv('medicos_dermacapelli.csv', sep=';', low_memory=False, encoding='latin-1')
# print(medicos.shape)
# medicos["id_import"] = medicos["id_import"].astype(str)
# medcomb = pd.merge(combinacao, medicos, left_on='CodMedico_x', right_on='id_import', how='inner')
# medcomb.to_csv('medcomb.csv', sep=';', escapechar='\\', quoting=csv.QUOTE_ALL, index=False, encoding='latin-1')
# print(medcomb.shape)

# 'PACIENTE_NOVO.csv', 'HISTORIC_NOVO.csv', 'PROFISS_NOVO.csv', 'medicos_dermacapelli.csv',

# for file in ['medcombDrop.csv']:
#     with open(file, 'r', encoding='latin-1') as arq:
#         print('#'*10)
#         reader = csv.DictReader(arq, delimiter=';')
#         headers = reader.fieldnames
#         print(headers)
#     arq.close()

# combinar = pd.merge(paciente, agenda, how='inner', on='CodPaciente')
# combinar.to_csv('combinacao.csv', index=False)
# print('#'*10)

# for file in ['PACIENTE_NOVO.csv', 'HISTORIC_NOVO.csv', 'combinacao.csv', 'PROFISS_NOVO.csv']:
#     with open(file, 'r', encoding='latin-1') as arq:
#         print('#'*10)
#         reader = csv.DictReader(arq, delimiter=';')
#         headers = reader.fieldnames
#         print(headers)
#
#     arq.close()




# INSERT INTO public.paciente(
# 	cel, (length = 60, String) Ex: (61) 33457646
# 	cpf, ( length = 90, String)  OBS: sem pontuação - Obrigatorio
# 	data_cadastro, (Date) - Obrigatorio
# 	email, (length = 255, String)
# 	endereco, (length = 255, String). Ex: QNN 19 CONJUNTO K CASA 14-,CEILANDIA,CEILANDIA/DF,72225201 - separados por ',' e cidade  e uf separados por '/'
# 	nascimento, (Date) - Obrigatorio
# 	nome, (length = 255, String) - Obrigatorio.
# 	profissao, (length = 255, String)
# 	sexo, (String, maiusculo) - Obrigatorio.
# 	status_p, (ACTIVED)
# 	tel, (length = 60, String) Ex: (61) 98117-4694
# 	flagagenda, (FALSE)
# 	compartilhar_prontuario, (FALSE)
# 	config_cadastro_completo, (NULL)
# 	cpf_obrigatorio, (FALSE)
# 	cartao_sus, (String)
# 	ucase_nome, (nome maiusculo)
# 	)
# 	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

# 	INSERT INTO public.paciente_clinica(
# 	paciente_id, clinica_id)
# 	SELECT id, 83 from paciente where id_paciente_dermacapelli = [%s];

# clinica 83


# INSERT INTO public.agenda(data_agendada,  data_agendada_timestamp, horario,
# descricao, etiqueta, status, status_consulta, confirm_consulta, codigo_saida,
# data_solicitacao, tipo_atendimento, is_encaixe, data_atendimento, data_finalizacao,
# responsavel_recepcao, paciente_online, fk_clinica_id, fk_medico_id, fk_paciente_id,
# fk_especializacao_id, fk_forma_atendimento_id, id_agendamento_visao, id_agendamento_pai_visao,
# fk_agendamento_pai_id) VALUES ('2021-05-26', '2021-05-26 08:00:00.0', '08:00', '', 'consulta',
# '1', 'AGUARDANDO', 'CONFIRMADO', 'RETORNO', '2021-05-26', 'CONSULTA', false, '2021-05-26',
# null, 'Edson Silvério da Silva', false, 30,
# (SELECT id FROM medico where medico.crm_uf='DF' and medico.crm='3902' LIMIT 1),
# (SELECT id FROM paciente where paciente.id_paciente_visao=245814 LIMIT 1),
# (SELECT id FROM precoespecializacao where precoespecializacao.fk_precoespecializacao_id=(SELECT id FROM medico where medico.crm_uf='DF' and medico.crm='3902' LIMIT 1) and precoespecializacao.fk_especialidade_id=42 LIMIT 1),
# (SELECT id FROM convenio where convenio.registroans='346659' LIMIT 1), 9808564, null, (null));

# - Primeiro Criar Agenda nos @
#  - Criar prontuario
#  - Criar permissao_ponrtuario clinica
#  - Criar insert Anamnese


# - Primeiro Criar Agenda nos @
# 	* Ver id das especialidades dos médicos (BD doctor)
# 	* Ver id das preco_especialização dos medicos com particular (BD doctor)
# 	* Colocar Status padrões na consulta
#  - Criar prontuario
#  - Criar permissao_ponrtuario clinica
#  - Criar insert Anamnese


# 20	Leonardo Spagnol Abraham
# 25	Sofia Sales
# 26	Ana Acioli de Queiroz
# 2	Melissa Chaves Azevedo e Silva


# id_medico_doctor	fk_precoespecializacao_id
# 203	                776
# 210	                798
# 213	                806
# 212	                804
# 214	                808
# 211	                801

# onde é null, tem que concatenar sem as aspas simples, e onde é fk as colunas são long ai tem que ser sem aspas simples tbm
# marca_de_verificação_branca
# olhos
# mãos_para_cima
#

# 11h18
# e onde é variavel booleano tbm

# INSERT INTO public.prontuario(datacriacao, fk_paciente_id) SELECT now(), id from PACIENTE where id_paciente_visao = 106073;
# id from PACIENTE where id_paciente_visao = 106073;
# esse where aqui vai ser na coluna id do seu banco que vai estar referenciado no banco da doctor


# INSERT INTO public.permissao_prontuario_clinica(modificado_em, fk_medico_id, fk_prontuario_id, fk_rede_clinica_id,
#                                                 escrita, leitura)
# VALUES (now(),
#         {idMedico na doctor},
#                     (SELECT id FROM public.prontuario WHERE fk_paciente_id = (SELECT id FROM paciente where paciente.id_paciente_dermacapelli={} LIMIT 1)),
# (SELECT fk_rede_clinica_id FROM public.clinica WHERE id = (83)), 'false', 'false');