
class gerador_primos():

	def retorna_primos():

		numero_max = int(input("Até que número irá a varredura:"))

		if numero_max < 1:
			print("Número Máximo Deve Ser Maior Que Zero.")	

		else:	
			for i in range(1,numero_max+1):

				contador = 0

				for j in range(2,i):

					if i % j == 0:
						contador += 1
						break

				if contador == 0:
					print (i, "é Número Primo")

gerador_primos.retorna_primos()