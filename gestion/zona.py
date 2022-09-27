from gestion.zoologico import Zoologico

class Zona:
    def __init__(self, nombre, zoo=None, animales=None):
        self.nombre=nombre
        self.zoo=zoo
        self.animales=animales
    def agregarAnimales(self, animal):
        if self.animales is None:
            self.animales=[]
        self.animales.append(animal)
    def cantidadAnimales(self):
        return len(self.animales)
    def getNombre(self):
        return self.nombre
    def getZoo(self):
        return self.zoo