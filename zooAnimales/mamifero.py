from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado=[]
    caballos=0
    leones=0
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje=pelaje
        self.patas=patas
        Mamifero.listado.append(self)
    def cantidadMamiferos():
        return Mamifero.listado.length()
    def crearCaballo(nombre, edad, genero):
        Mamifero(nombre, edad, "pradera", genero, True, 4)
        Mamifero.caballos+=1
    def crearLeon(nombre, edad, genero):
        Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.leones+=1
    def isPelaje(self):
        return self.pelaje
    def getPatas(self):
        return self.patas