#Calculadora PYTHON - Desenvolvedor: Roger Luiz

import math
def soma(x,y):
  return x+y
def subtracao(x,y):
  return x-y
def multiplicacao(x,y):
  return x*y
def divisao (x,y):
  return x/y
def potencia (x,y):
  return x**y
def raiz (x):
  return math.sqrt(x)

print("CALCULADORA EM PYTHON: \n")
print("Digite 1 para Soma.")
print("Digite 2 para Subtração. ")
print("Digite 3 para Multiplicação.")
print("Digite 4 para Divisão.")
print("Digite 5 para Potencia.")
print("Digite 6 para Raiz Quadrada.\n")

valores=input("Digite o comando aqui: \n")
num1=int(input("Agora digite o primeiro número:\n "))
num2=int(input("Agora digite o segundo número aqui:\n "))

if valores == '1':
  print(num1, "+", num2, "=", soma(num1,num2))
elif valores == '2':
  print(num1, "-", num2, "=", subtracao(num1,num2))
elif valores == '3':
  print(num1, "*", num2, "=", multiplicacao(num1,num2))
elif valores == '4':
  print(num1, "/", num2, "=", divisao(num1,num2))
elif valores == '5':
  print(num1, "^", num2, "=", potencia(num1,num2))
elif valores == '6':
  print("Raiz quadrada de: ", num1, "=", raiz(num1))
else:
  print("Opção não disponível")