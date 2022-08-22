'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
geral = list()
pessoas = list()
maior = menor = 0

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(geral) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    geral.append(pessoas[:])
    pessoas.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('=-' * 30)
print(f'Os dados foram {geral}')
print(f'Ao todo foram {len(geral)} pessoas cadastradas.')
print(f'O maior peso é de {maior}Kg. Peso de ', end='')

for p in geral:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()

print(f'O menor peso é de {menor}Kg. Peso de ', end='')

for p in geral:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()

















