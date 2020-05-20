#LAB03 Jogo da Forca

import random
import os

clear = lambda: os.system('cls')

tabuleiro = ['''
   +---+
   |   |
       |
       |
       |
       |
  ==========''','''
   +---+
   |   |
   O   |
       |
       |
       |
  ==========''',"""
   +---+
   |   |
   O   |
   |   |
       |
       |
  ==========""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
  ==========""","""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
       |
  ==========""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
       |
  ==========""","""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
       |
       |
  ==========""","""
   +---+
   |   |
   O   |
  ---  |
  /|\  |
  / \  |
       |
       |
       |
  =========="""
]

def escolha_palavra():

		arq = open('palavras_new.txt','rt',encoding='cp1252')
		arq = arq.read()
		palavras_totais = arq.split('\n')
		palavra = palavras_totais[random.randint(0,len(arq.split('\n'))-1)]
		return palavra

class dinamica_jogo():

	def __init__(self,palavra):
		self.palavra = palavra
#		print(palavra)
	
	def letra(letra='a'):
		return input("Digite sua letra gentil senhor: \n")
		
	def comparacao(letra,palavra,letras_tentadas):
		
		if letra in palavra and letras_tentadas.count(letra) == 1:
			return 0
		else: 
			return 1

def solicitacao():

	palavra_escolhida = dinamica_jogo(escolha_palavra())

	contador_erros = 0
	contador_acertos = 0

	print('\n')
	print(tabuleiro[contador_erros])
	print('\n')
	palavra_incompleta = ('   '+('_'*len(palavra_escolhida.palavra)))
	print(palavra_incompleta)
	print('\n')	

	letras_tentadas = []

	while contador_erros < 7 and contador_acertos < int(len(set(palavra_escolhida.palavra))):
		
		letra_escolhida = dinamica_jogo.letra()
		letras_tentadas.append(letra_escolhida)
		atualiza_contador = dinamica_jogo.comparacao(letra_escolhida,palavra_escolhida.palavra,letras_tentadas)		
		contador_erros += atualiza_contador

		if atualiza_contador == 1:

			clear()
		
			print('\n')
			print('Muito burro o senhor. Deve estar assistindo muito live da Anitta.')
			print('\n')
			print("Letras Tentadas:",set(letras_tentadas))
			print('\n')
			print(tabuleiro[contador_erros])
			print('\n')

		else:
		
			clear()
			
			print('\n')
			print('Parabéns. Pelo visto, o senhor é catedrático na lingua pátria.')
			print('\n')
			print("Letras Tentadas:",set(letras_tentadas))
			print('\n')
			print(tabuleiro[contador_erros])
			print('\n')
			contador_acertos += 1

			if contador_acertos == int(len(set(palavra_escolhida.palavra))):
				print('\n')
				print("Fantástica performance... você só pode ser são paulino. \n A palavra final era:")
				print('\n')
			else:
				pass

			for i in list(pos for pos, x in enumerate('   ' + palavra_escolhida.palavra) if x == letra_escolhida):
				palavra_auxiliar = list(palavra_incompleta)
				palavra_auxiliar[i] = letra_escolhida
				palavra_incompleta = "".join(palavra_auxiliar)
			
		print('\n')
		print(palavra_incompleta)
		print('\n')

	if contador_erros == len(tabuleiro)-1: #int(len(set(palavra_escolhida.palavra))):
		print('\n')
		print("Misericórdia... anta igual a você, nunca vi. \n A palavra final era:")
		print('\n')
		print('   ' + palavra_escolhida.palavra)
	
	else:
		pass


clear()							
solicitacao()

#myString = 'Position of a character'
#x=list(pos for pos, x in enumerate(myString) if x == 'a')
#y=x[1]
#print(type(y))

#print(list(pos for pos, x in enumerate(myString) if x == 'a'))
#print(list(myString)[1,2,5])

#teste = 'aaaa'
#print(teste.replace('a','x',-1))














