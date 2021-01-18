""" def funcion_decoradora(funcion):

	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")

	return wrapper

def zumbido():

	print("Buzzzzzz")

zumbido = funcion_decoradora(zumbido) """


# Esta es una mejor forma que ofrece Python:

def funcion_decoradora(funcion):

	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")

	return wrapper

@funcion_decoradora
def zumbido():
	print("Buzzzzzz")

zumbido()