import math

print("+ = soma \n"
      "- = subtração \n"
      "* = multiplicação \n"
      "/ = divisão \n"
      "** = potenciação \n"
      "^ = radiciação \n"
      "log = logaritmo")

print("\n")

numero1 = float(input('Digite o primeiro número: \n'))
operacao = str(input('Digite o símbolo da operção: \n'))
numero2 = float(input('Digite o segundo número: \n'))

print("\n")

if operacao == '+':
  resultado = numero1 + numero2
  print(f'{numero1} + {numero2} = {resultado}')
elif operacao == '-':
  resultado = numero1 - numero2
  print(f'{numero1} - {numero2} = {resultado}')
elif operacao == '*':
  resultado = numero1 * numero2
  print(f'{numero1} * {numero2} = {resultado}')
elif operacao == '/':
  try:
    resultado = numero1 / numero2
    print(f'{numero1} / {numero2} = {resultado}')
  except ZeroDivisionError:
    print("Zero não divide")
    print("Tente novamente")
elif operacao == '**':
  resultado = math.pow(numero1, numero2)
  print(f'{numero1} ** {numero2} = {resultado}')
elif operacao == '^':
  resultado = math.pow(numero1, (1/numero2))
  print(f'{numero1} ^ {numero2} = {resultado}')
elif operacao == 'log':
  resultado = math.log(numero1, numero2)
  print(f'log {numero1} base {numero2} = {resultado}')
else:
  print("Operação Inválida")