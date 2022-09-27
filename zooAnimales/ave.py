from zooAnimales.animal import Animal

class Ave(Animal):
    listado=[]
    halcones=0
    aguilas=0
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPlumas=colorPlumas
        Ave.listado.append(self)
    def cantidadAves():
        return len(Ave.listado)
    def crearHalcon(nombre, edad, genero):
        Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        Ave.halcones+=1
    def crearAguila(nombre, edad, genero):
        Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        Ave.aguilas+=1
    def movimiento():
        return "volar"
    def getColorPlumas(self):
        return self.colorPlumas