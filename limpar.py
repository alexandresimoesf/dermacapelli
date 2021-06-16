import csv
# encoding utf-8 para profiss e latin-1 para outros
codigos = []
with open('HISTORIC_original.csv', 'r', encoding='latin-1') as arq:
    reader = csv.DictReader(arq, delimiter=';')
    headers = reader.fieldnames
    with open('HISTORIC_NOVO.csv', 'w', newline='\n') as novo:
        writer = csv.DictWriter(novo, delimiter=';', fieldnames=headers)
        writer.writeheader()
        for linha in reader:
            for i, j in linha.items():
                try:
                    if i == 'CodPaciente' and j == '':
                        j = j.replace('', 'null')
                        linha[i] = j
                    if j == '':
                        j = j.replace('', 'null')
                        linha[i] = j
                    if '\'' in j:
                        j = j.replace('\'', 'null')
                        linha[i] = j
                    if '_' in j:
                        j = j.replace('_', '0')
                        linha[i] = j
                    if '\"' in j:
                        j = j.replace('\"', 'null')
                        linha[i] = j
                    if '|' in j:
                        j = j.replace('|', '')
                        linha[i] = j
                except:
                    pass
            try:
                writer.writerow(linha)
            except Exception as e:
                pass
                # codigos.append(linha['CodPaciente'])
        arq.close()
        novo.close()

print(codigos)

# # encoding utf-8 para profiss e latin-1 para outros
#
# with open('PROFISS.csv', 'r', encoding='utf-8') as arq:
#     reader = csv.DictReader(arq, delimiter=';')
#     headers = reader.fieldnames
#     with open('PROFISS_NOVO.csv', 'w', newline='\n') as novo:
#         writer = csv.DictWriter(novo, delimiter=';', fieldnames=headers)
#         writer.writeheader()
#         for linha in reader:
#             for i, j in linha.items():
#                 if i == 'CodPaciente' and j == '':
#                     j = j.replace('', 'null')
#                     linha[i] = j
#                 if j == '':
#                     j = j.replace('', 'null')
#                     linha[i] = j
#                 if '\'' in j:
#                     j = j.replace('\'', 'null')
#                     linha[i] = j
#                 if '_' in j:
#                     j = j.replace('_', '0')
#                     linha[i] = j
#                 if '\"' in j:
#                     j = j.replace('\"', 'null')
#                     linha[i] = j
#                 if '|' in j:
#                     j = j.replace('|', '')
#                     linha[i] = j
#             try:
#                 writer.writerow(linha)
#             except Exception as e:
#                 print(linha, e)
#         arq.close()
#         novo.close()
#

