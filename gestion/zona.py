from gestion.zoologico import Zoologico

class Zona:
    def __init__(self, nombre, zoo="none", animales=[]):
        self.nombre=nombre
        self.zoo=zoo
        self.animales=animales
    def agregarAnimales(self, animal):
        self.animales.append(animal)
    def cantidadAnimales(self):
        return self.animales.length()