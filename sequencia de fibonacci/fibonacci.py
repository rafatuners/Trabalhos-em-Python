numero1 = int(0)
numero2 = int(1)
numero3 = int(0)

Valor = int(input('Digite um número: '))
while (Valor > numero3):
    numero3 = numero1 + numero2
    numero1 = numero2
    numero2 = numero3

if (Valor == 0 or Valor == 1):
    print ('O número faz parte da sequência de Fibonacci.')
elif (Valor == numero3):
    print ('O número faz parte da sequência de Fibonacci.')
else:
    print ('O número digitado não faz parte da sequência de Fibonacci.')