'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter


jogo = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}

print(f'{"Valores sorteados:":-^30}:')
ranking = list()

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print()
print(f'{"Ranking":-^30}:')
for n, v in enumerate(ranking):
    print(f'{n+1}ºLugar: {v[0]} com {v[1]}.')
    sleep(1)





