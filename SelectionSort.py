import random as rd

class selection_sort():

	def sequencia():

		seq_min = int(input("Digite o número mínimo para ordenacao:"))
		seq_max = int(input("Digite o número máximo para ordenacao:"))
		num_seq = int(input("Digite a quantidade de sequencia:"))

		sequencia_aux = []
		sequencia_aux.append([rd.randint(seq_min, seq_max) for x in range(num_seq)])
		sequencia = [item for sequencia in sequencia_aux for item in sequencia]
#		sequencia = list(enumerate(list(sequencia)))

		return sequencia

	def ordenacao(sequencia):

		ordenacao = [0] * len(sequencia)

		for i in range(len(sequencia)):#[x[0] for x in a]:
			print("novo ciclo \n")
			print(i)
			print(sequencia)
			
			if  i < len(sequencia) - 1 and sequencia[i] <= min(sequencia[i+1:]):
					ordenacao[i] = sequencia[i]

			elif  i == len(sequencia): #and sequencia[i] <= min(sequencia[i:]):
					ordenacao[i] = sequencia[i]
			else:
				ordenacao[i] = min(sequencia[i:])
				print(sequencia[i:].index(min(sequencia[i:])))
				sequencia[sequencia[i:].index(min(sequencia[i:])) + i] = sequencia[i]

			print('\n')
			print(ordenacao)
			print(sequencia,'\n')

a = selection_sort.sequencia()
print(a)
b = selection_sort.ordenacao(a)


		
