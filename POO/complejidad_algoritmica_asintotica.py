# En Big O Notation solo nos interesa el coeficiente más grande sin ningún tipo de coeficiente previo

# Ley de la suma

def f(n):

    for i in range(n): # n operaciones
        print(i)

    for i in range(n): # n operaciones
        print(i)


# O(n) + O(n) = O(n + n) = O(2n) 
# Como en Big O no importan los coeficientes, podemos simplificar: 0(2n)= O(n) por lo que podemos decir que la función crece de forma linea con respecto a "n"



# Ley de la suma

def f(n):

    for i in range(n): # n operaciones
        print(i)

    for i in range(n * n): # n * n operaciones
        print(i)


# O(n) + O(n * n) = O(n + n²) = O(n²) Esta función crece de manera cuadrática con respecto a n



# Ley de la multiplicación

def f(n):

    for i in range(n): # n² operaciones
        for i in range(n * n): 
            print(i, j)


# O(n) * O(n) = O(n * n) = O(n²) Esta función crece de manera cuadrática con respecto a n



# Recursividad múltiple

def fibonacci(n):

    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# O(2**n) Esta función crece de manera exponencial con respecto a "n " ya que la función se vuelve a llamar dos veces cada vez que n no es 0 o 1