import random as rd
import numpy as np
import time as tm
import sys

class robo_vitcongue():

	def nivel_acao():
		print('\n')
		linha = int(input("Quantas linhas terão os tabuleiro? \n"))
		print('\n')
		coluna = int(input("Quantas colunas terão os tabuleiro? \n"))
		print('\n')
		dificuldade = int(input("Qual o nível de dificuldade do campo minado: \n 1 Fácil \n 2 para Trincheiras da PGM (Díficil, mas possível) \n 3 para Invadir a Russia no Inverno \n"))
		print('\n')
		if dificuldade == 1:
			minas_terrestres = int(linha * coluna * 0.1)

		if dificuldade == 2:
			minas_terrestres = int(linha * coluna * 0.2)

		if dificuldade == 3:
			minas_terrestres = int(linha * coluna * 0.3)

		return linha, coluna, minas_terrestres

	def tabuleiro(linha,coluna,minas_terrestres):

		tabuleiro = []

		for i in range(linha):
			linhas = []

			for j in range(coluna):
				linhas.append("0")

			tabuleiro.append(linhas)

		posicao = [[]]

		while len(posicao) <= minas_terrestres:
			l = rd.randint(0, linha-1)
			c = rd.randint(0, coluna-1)
			
			posicao.append([l,c])

		for i in range(1,minas_terrestres+1):
			tabuleiro[posicao[i][0]][posicao[i][1]] = "X"

		return tabuleiro

	def caminho(tabuleiro):

		tabuleiro[0][0] = "R"
		tabuleiro[len(tabuleiro)-1][len(tabuleiro[0])-1] = "S"

		d = rd.randint(0, 1)
		
		col_ini = 0
		lin_ini = 0

		print('\n')
		print(np.matrix(tabuleiro))
		print('\n')					
		tm.sleep(2)
		
		if d == 0:
			for l in range(lin_ini,len(tabuleiro)):
				for c in range(col_ini,len(tabuleiro[0])):
					print(l)
					print(c)

					if l < len(tabuleiro) - 1 and c < len(tabuleiro[0]) - 1:
	
						if tabuleiro[l][c+1] == '0':
							tabuleiro[l][c] = '.'
							#tabuleiro = [[item.replace("R","0") for item in item_aux] for item_aux in tabuleiro]
							tabuleiro[l][c+1] = 'R'

							print('\n')
							print(np.matrix(tabuleiro))
							print('\n')					
							tm.sleep(2)

#							if c == len(tabuleiro[0]) - 2:
#								col_ini = len(tabuleiro[0]) - 1
#								break

						elif tabuleiro[l][c+1] == 'X' and tabuleiro[l+1][c] == '0':
							tabuleiro[l][c] = '.'
							#tabuleiro = [[item.replace("R","0") for item in item_aux] for item_aux in tabuleiro]
							tabuleiro[l+1][c] = 'R'
							lin_ini = l + 1
							col_ini = c

							print('\n')
							print(np.matrix(tabuleiro))
							print('\n')					
							tm.sleep(2)

							break

						elif tabuleiro[l][c+1] == 'X' and tabuleiro[l+1][c] == 'X':
							print('Explosão!')
							sys.exit()

					elif l == len(tabuleiro) - 1 and c < len(tabuleiro[0]) - 1:
						
						if tabuleiro[l][c+1] == 'X':
							print('Explosão!')
							sys.exit()

						else:
							tabuleiro[l][c+1] = 'R'
							tabuleiro[l][c] = '.'

							print('\n')
							print(np.matrix(tabuleiro))
							print('\n')					
							tm.sleep(2)

					elif l < len(tabuleiro) - 1 and c == len(tabuleiro[0]) - 1:
						
						if tabuleiro[l+1][c] == 'X':
							print('Explosão!')
							sys.exit()

						else:
							tabuleiro[l+1][c] = 'R'
							tabuleiro[l][c] = '.'

							col_ini = len(tabuleiro[0]) - 1

							print('\n')
							print(np.matrix(tabuleiro))
							print('\n')					
							tm.sleep(2)

					elif l == len(tabuleiro) - 1 and c == len(tabuleiro[0]) - 1 and tabuleiro[l][c] == 'R':

						print("Parabéns!") 
						sys.exit()

		else:
			for c in range(col_ini,len(tabuleiro[0])):
				for l in range(lin_ini,len(tabuleiro)):
					print(l)
					print(c)

					if l < len(tabuleiro) - 1 and c < len(tabuleiro[0]) - 1:
	
						if tabuleiro[l+1][c] == '0':
							tabuleiro[l][c] = '.'
							#tabuleiro = [[item.replace("R","0") for item in item_aux] for item_aux in tabuleiro]
							tabuleiro[l+1][c] = 'R'

							print('\n')
							print(np.matrix(tabuleiro))
							print('\n')					
							tm.sleep(2)

#							if c == len(tabuleiro[0]) - 2:
#								col_ini = len(tabuleiro[0]) - 1
#								break

						elif tabuleiro[l+1][c] == 'X' and tabuleiro[l][c+1] == '0':
							tabuleiro[l][c] = '.'
							#tabuleiro = [[item.replace("R","0") for item in item_aux] for item_aux in tabuleiro]
							tabuleiro[l][c+1] = 'R'
							lin_ini = l 
							col_ini = c + 1

							print('\n')
							print(np.matrix(tabuleiro))
							print('\n')					
							tm.sleep(2)

							break

						elif tabuleiro[l+1][c] == 'X' and tabuleiro[l][c+1] == 'X':
							print('Explosão!')
							sys.exit()

					elif l == len(tabuleiro) - 1 and c < len(tabuleiro[0]) - 1:
						
						if tabuleiro[l][c+1] == 'X':
							print('Explosão!')
							sys.exit()

						else:
							tabuleiro[l][c+1] = 'R'
							tabuleiro[l][c] = '.'

							print('\n')
							print(np.matrix(tabuleiro))
							print('\n')					
							tm.sleep(2)

					elif l < len(tabuleiro) - 1 and c == len(tabuleiro[0]) - 1:
						
						if tabuleiro[l+1][c] == 'X':
							print('Explosão!')
							sys.exit()

						else:
							tabuleiro[l+1][c] = 'R'
							tabuleiro[l][c] = '.'

							lin_ini = len(tabuleiro) - 1

							print('\n')
							print(np.matrix(tabuleiro))
							print('\n')					
							tm.sleep(2)

					elif l == len(tabuleiro) - 1 and c == len(tabuleiro[0]) - 1 and tabuleiro[l][c] == 'R':

						print("Parabéns!")
						sys.exit()

b = robo_vitcongue.nivel_acao()
a = robo_vitcongue.tabuleiro(b[0],b[1],b[2])
c = robo_vitcongue.caminho(a)

#print(type(a))
#print(np.matrix(a))















