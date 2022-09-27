class Zoologico:
    def __init__(self, nombre, ubicacion, zonas=[]):
        self.nombre=nombre
        self.ubicacion=ubicacion
        self.zonas=zonas
    def agregarZonas(self, zona):
        self.zonas.append(zona)
    def cantidadTotalAnimales(self):
        from zooAnimales.animal import Animal
        return Animal.totalAnimales
    def getZona(self):
        return self.zonas
    def getNombre(self):
        return self.nombre