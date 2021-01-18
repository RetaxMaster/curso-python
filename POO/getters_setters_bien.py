# Usando el decorator @propery

class CasillaDeVotacion:
    

    def __init__(self, identificador, pais):
        
        self._identificador = identificador
        self._pais = pais
        self._region = None


    @property
    def region(self):
        return self._region


    @region.setter
    def region(self, region_name):
        if region_name in self._pais:
            self._region = region_name
        else:
            raise ValueError(f'La region {region_name} no esta en la lista')


casilla = CasillaDeVotacion(123,['Mexico','Morelos'])
print(casilla.region)

casilla.region = 'Mexico'
print(casilla.region)
