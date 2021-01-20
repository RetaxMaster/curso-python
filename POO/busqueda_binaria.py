import random

def busqueda_binaria(lista, comienzo, final, objetivo, c = 0):

    print(f"Buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}, paso #{c + 1}")

    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True

    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, c + 1)
    
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, c + 1)



if __name__ == "__main__":
    
    tamano_de_lista = int(input("¿De qué tamaño será la lista?: "))
    objetivo = int(input("¿Qué múmero quieres encontrar?: "))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f"El elemento {objetivo} {'esta' if encontrado else 'no esta'}")