#ciclos

#for elemento in lista
def iterar(l):
	for x in l: #para toda x en la lista l
		print(x)

lista = [1,2,3,4,5]
print("for")
iterar(lista)

def iterar(l):
	#puedo acotar cuales elementos de l voy a procesar
	for x in l[:-1]: #para toda x en l menos el ultimo
		print(x)

print("for -1")
iterar(lista)

#while(condicion)
def iteraWhile(condicion):
	while(condicion):
		print(":D")

#iteraWhile(True) #ciclo infinito

def iteraWhile(l):
	i = 0
	n = len(l) #el tamano de la lista l
	while i < n: #mientras que i < n
		print(l[i]) #imprime el i-esimo elemento de l
		i = i+1 #actualiza i

print("while")
iteraWhile(lista)