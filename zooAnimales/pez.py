from zooAnimales.animal import Animal

class Pez(Animal):
    listado=[]
    salmones=0
    bacalaos=0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas=colorEscamas
        self.cantidadAletas=cantidadAletas
        Pez.listado.append(self)
    def cantidadPeces():
        return len(Pez.listado)
    def crearSalmon(nombre, edad, genero):
        Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.salmones+=1
    def crearBacalao(nombre, edad, genero):
        Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.bacalaos+=1
    def movimiento():
        return "nadar"
    def getColorEscamas(self):
        return self.colorEscamas
    def getCantidadAletas(self):
        return self.cantidadAletas
