import os
import math

print('+ = Adição \n'
      '- = Subtração \n'
      '* = Multipicação \n'
      '/ = Divisão \n'
      '** = Potenciação \n'
      '^ = Radiação \n'
      'log = Logaritmo \n')

primeiro_numero = float(input('Primeiro número: '))
operacao = str(input('Operação: '))
segundo_numero = float(input('Segundo número: '))

os.system('cls') or None

if operacao == '+':
    try:
        resultado = primeiro_numero + segundo_numero
        print(f'{primeiro_numero} + {segundo_numero} = {resultado}')
    except OverflowError:
        print("Error: Números muito grandes")
elif operacao == '-':
    try:
        resultado = primeiro_numero - segundo_numero
        print(f'{primeiro_numero} - {segundo_numero} = {resultado}')
    except OverflowError:
        print("Error: Números muito grandes")
elif operacao == '*':
    try:
        resultado = primeiro_numero * segundo_numero
        print(f'{primeiro_numero} * {segundo_numero} = {resultado}')
    except OverflowError:
        print("Error: Números muito grandes")
elif operacao == '/':
    try:
        resultado = primeiro_numero / segundo_numero
        print(f'{primeiro_numero} / {segundo_numero} = {resultado}')
    except ZeroDivisionError:
        print("Error: Zero não divide")
    except OverflowError:
        print("Error: Números muito grandes")
elif operacao == '**':
    try:
        resultado = math.pow(primeiro_numero, segundo_numero)
        print(f'{primeiro_numero} ** {segundo_numero} = {resultado}')
    except OverflowError:
        print("Error: Números muito grandes")
elif operacao == '^':
    try:
        resultado = math.pow(primeiro_numero, 1/segundo_numero)
        print(f'{primeiro_numero} ^ {segundo_numero} = {resultado}')
    except OverflowError:
        print("Error: Números muito grandes")
elif operacao == 'log' or operacao == 'loG' or operacao == 'lOg' or operacao == 'Log' or operacao == 'LOg' or operacao == 'lOG' or operacao == 'LoG' or operacao == 'LOG':
    try:
        resultado = math.log(primeiro_numero, segundo_numero)
        print(f'log de {primeiro_numero} com base {segundo_numero} = {resultado}')
    except OverflowError:
        print("Error: Números muito grandes")
else:
    print('Operação inválida')
