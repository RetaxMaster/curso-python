def factorial(n):

    """
    Calcula el factorail de n.

    n int > 0
    return n!
    """
    if n == 1:
        return 1

    return n * factorial(n - 1)

n = int(input("Escribe un entero: "))
print(f"El factorial de {str(n)} es {factorial(n)}")

