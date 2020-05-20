import math
import numpy
import random
import statistics
from functools import reduce


def multiplicacao(x,y):
	return (x * y)

def divisao(x,y):
	return (x / y)

def adicao(x,y):
	return (x + y)

def subtracao(x,y):
	return (x - y)

def potencia(x,y):
	return (x ** y)

def num_primo(y):
	x = int(y)
	contador = 0
	if x <= 0:
		print ('Número Negativo Não É Primo')
	elif x == 1:
		print('Número Primo')
	else:
		for i in range (1,x):
			if x % i == 0:
				contador += 1
		if contador == 1:
			print ('Número Primo')
		else:
			print('Número Não É Primo')

var1 = input('Digite a operação desejada: \n 1 - Multiplicação \n 2 - Divisão \n 3 - Adição \n 4 - Subtração \n 5 - Potência \n 6 - Números Primos \n')

opcoes = ['1','2','3','4','5','6']

if var1 in opcoes:
	pass
else:
	while var1 not in opcoes:
		print ('Operação Inválida')
		var1 = input('Digite a operação desejada: \n 1 - Multiplicação \n 2 - Divisão \n 3 - Adição \n 4 - Subtração \n 5 - Potência \n 6 - Números Primos \n')
		if var1 == 'Kill':
			break

var2 = input('Digite o primeiro algarismo da operação: ')
var2 = int(var2)

var3 = input('Digite o segundo algarismo da operação: ')
var3 = int(var3)

if var1 == '1':
	print(multiplicacao(var2,var3))
elif var1 == '2':
	print(divisao(var2,var3))
elif var1 == '3':
	print(adicao(var2,var3))
elif var1 == '4':
	print(subtracao(var2,var3))
elif var1 == '5':
	print(potencia(var2,var3))
else:
	print(num_primo(var2))
	print(num_primo(var3))