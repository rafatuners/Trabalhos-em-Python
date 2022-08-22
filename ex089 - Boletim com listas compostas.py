'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.
'''
from time import sleep
boletim = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print('=-' * 40)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 40)

for i, aluno in enumerate(boletim):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
print('-' * 40)

while True:
    opc = int(input('Mostrar notas de qual aluno? (digite 999 para encerrar). '))
    if opc == 999:
        break
    if opc <= len(boletim) - 1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')

print('Finalizando....')
sleep(1)
print('Volte sempre!')


