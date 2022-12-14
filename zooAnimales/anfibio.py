from zooAnimales.animal import Animal

class Anfibio(Animal):
    listado=[]
    ranas=0
    salamandras=0
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPiel=colorPiel
        self.venenoso=venenoso
        Anfibio.listado.append(self)
    def cantidadAnfibios():
        return len(Anfibio.listado)
    def crearRana(nombre, edad, genero):
        Anfibio.ranas+=1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras+=1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
    def movimiento():
        return "saltar"
    def getColorPiel(self):
        return self.colorPiel
    def isVenenoso(self):
        return self.venenoso