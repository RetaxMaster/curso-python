# Aquí medimos los pasos (la cantidad de operaciones que hace el algoritmo)

def f(x):

    respuesta = 0 # 1 operación

    for i in range(1000): # 1000 operaciones
        respuesta +=1

    for i in range(x): # x operaciones
        respuesta +=1

    for i in range(x):      # 2x² operaciones
        for j in range(x):
            respuesta +=1
            respuesta +=1

    return respuesta # 1 operacion

# Podemos concluir que el número de operaciones de este algoritmo está dado por la ecuación 1002 + x + 2x² (1002 sale de la suma de las 1000 operaciones mas las otras 2 operaciones que tenemos por ahí), podemos ver como a medida que x crece, la parte que más operaciones va a realizar es la de 2x²