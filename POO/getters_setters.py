class Millas:

	def __init__(self, distancia = 0):
		self.distancia = distancia


	def convertir_a_kilometros(self):
		return (self.distancia * 1.609344)


	# Método getter
	def obtener_distancia(self):
		return self._distancia


	# Método setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		self._distancia = valor

# Usando property(fget, fset, fdel, fdoc) :

class Millas2:

	def __init__(self):
		self._distancia = 0


	# Función para obtener el valor de _distancia
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia


	# Función para definir el valor de _distancia
	def definir_distancia(self, recorrido):
		print("Llamada al método setter")
		self._distancia = recorrido


	# Función para eliminar el atributo _distancia
	def eliminar_distancia(self):
		del self._distancia


	distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

# Creamos un nuevo objeto 
avion = Millas2()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos su atributo distancia
print(avion.distancia)
# Llamada al método getter
# Llamada al método setter
# 200 

# Usando el decorador @property (dudo que funcione...)

class Millas3:

	def __init__(self):
		self._distancia = 0


	# Función para obtener el valor de _distancia
	# Usando el decorador property
	@property
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia


	# Función para definir el valor de _distancia
	@distancia.setter
	def definir_distancia(self, valor):

		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")

		print("Llamada al método setter")
		self._distancia = valor

# Creamos un nuevo objeto 
avion = Millas3()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos su atributo distancia
print(avion.distancia)
# Llamada al método getter
# Llamada al método setter
# 200

