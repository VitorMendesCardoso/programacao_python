class UniqueChars(object):

    def has_unique_chars(self, string):
        # Implemente aqui sua solução
        letras_distintas = set(string)

        if len(letras_distintas) == len(string):
        	return True
        else:
        	return False

teste = UniqueChars()
teste = teste.has_unique_chars("FOoO")
print(teste)