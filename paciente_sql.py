import csv
import re
import unidecode
import pandas as pd

# #
# comb = pd.read_csv('medcomb.csv', sep=';', encoding='latin-1', dtype='unicode')
# print(comb.shape)
# combDist = comb.drop_duplicates(subset=['CodPaciente'], keep='first')
# combDist.to_csv('medcombDrop.csv', sep=';', escapechar='\\', quoting=csv.QUOTE_ALL, index=False, encoding='latin-1')
# print(combDist.shape)

listaBug = ['1444', '2572', '2687', '3237', '3531', '3561', '3657', '3657',
            '3746', '4240', '4360', '4670', '6133', '6800', '9156', '9591',
            '14077', '14968', '15526', '15528', '15597', '15615', '15620',
            '15621', '15633', '15651', '15653', '16603', '16807', '17036',
            '17409', '17486', '17486', '17716', '18158']


with open('PACIENTE_NOVO.csv', 'r', newline='\n', encoding='latin-1') as file:
    sql = open('paciente_sql_junto.sql', 'w', encoding='latin-1')
    reader = csv.DictReader(file, delimiter=';')
    sqlInicio = 'INSERT INTO public.paciente('
    colunas = 'id_paciente_dermacapelli, cel, data_cadastro, ' \
              'nascimento, ' \
              'nome, profissao, sexo, status_P, ' \
              'tel, flagagenda, compartilhar_prontuario, ' \
              'config_cadastro_completo, cpf_obrigatorio, ' \
              'ucase_nome) VALUES ('
    for n, linha in enumerate(reader):
        try:
            id = linha['CodPaciente']
            cel = ''.join(re.findall("\d+", linha['Fone']))
            data_cadastro = '{}{}{}{}/{}{}/{}{}'.format(*linha['DtEntrada'])
            endereco = linha['Endereco'].encode('utf-8').decode('latin-1')
            cep = int(float(linha['CEP']))
            cidade = linha['Cidade'].encode('utf-8').decode('latin-1')
            endereco = '{},{},{}/{},{}'.format(endereco, cidade, cidade, linha['Estado'], cep)
            if len(linha['MesDiaNascimento']) == 3:
                nascimento = '{}{}{}{}/0{}/{}{}'.format(*linha['AnoNascimento'], *linha['MesDiaNascimento'])
            else:
                nascimento = '{}{}{}{}/{}{}/{}{}'.format(*linha['AnoNascimento'], *linha['MesDiaNascimento'])
            nome = linha['Nome']
            profissao = unidecode.unidecode(linha['Profissao']) # .encode('utf-8').decode('latin-1')
            sexo = 'MASCULINO' if linha['Sexo'] == 'M' else 'FEMININO'
            status_p = 'ACTIVED'
            tel = cel
            flagagenda = 'FALSE'
            compartilhar_prontuario = 'FALSE'
            config_cadastro_completo = 'Null'
            cpf_obrigatorio = 'FALSE'
            ucase_nome = linha['Nome'].upper()

            sqlConteudo = "{} ,'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(
                id, cel, data_cadastro,
                nascimento, nome,
                profissao, sexo, status_p,
                tel, flagagenda, compartilhar_prontuario,
                config_cadastro_completo, cpf_obrigatorio,
                ucase_nome)
            if linha['AnoNascimento'] != '0000' and linha['DtEntrada'] != '0000':
                sql.write('{}{}{}\n'.format(sqlInicio, colunas, sqlConteudo))
                sql.write('INSERT INTO public.paciente_clinica(paciente_id,'
                          ' clinica_id) SELECT id, 83 from public.paciente WHERE paciente.id_paciente_dermacapelli = {};\n'.format(id))
        except Exception as e:
            pass
            # print(e)
            # print('#' * 10)
    sql.close()

# 	INSERT INTO public.paciente_clinica(
# 	paciente_id, clinica_id)
# 	SELECT id, 83 from paciente where id_paciente_dermacapelli = [%s];