# Los tests de cristal validan todos los caminos, tanto de un if que si pasa, un if que no pasan, etc. Aquí tienes que conocer cómo está construida la función

import unittest


def es_mayor_de_edad(edad):

    if edad >= 18:
        return True
    else:
        return False


class CajaNegraTest(unittest.TestCase):
    

    def test_es_mayor_de_edad(self):

        edad = 20
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, True)


    def test_es_menor_de_edad(self):

        edad = 15
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, False)



if __name__ == "__main__":
    unittest.main()
