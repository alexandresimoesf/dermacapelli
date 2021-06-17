import csv
from collections import deque

def meu_arquivo():
    with open('HISTORIC_NOVO.csv', 'r', encoding='latin-1') as arquivo:
        leitura = deque(csv.DictReader(arquivo))
        for i in leitura:
            print(i)