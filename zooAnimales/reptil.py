from zooAnimales.animal import Animal

class Reptil(Animal):
    listado=[]
    iguanas=0
    serpientes=0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas=colorEscamas
        self.largoCola=largoCola
        Reptil.listado.append(self)
    def cantidadReptiles():
        return len(Reptil.listado)
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes+=1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas+=1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)
    def movimiento():
        return "reptar"
    def getColorEscamas(self):
        return self.colorEscamas
    def getLargoCola(self):
        return self.largoCola