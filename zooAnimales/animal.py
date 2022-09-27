from gestion.zona import Zona

class Animal:
    totalAnimales=0
    def __init__(self, nombre, edad, habitat, genero, zona="none"):
        self.nombre=nombre
        self.edad=edad
        self.habitat=habitat
        self.genero=genero
        self.zona=zona
        Animal.totalAnimales+=1
    def movimiento():
        return "desplazarse"
    def totalPorTipo():
        from zooAnimales import Mamifero
        from zooAnimales import Ave
        from zooAnimales import Anfibio
        from zooAnimales import Reptil
        from zooAnimales import Pez
        resultado=("Mamiferos: ",Mamifero.cantidadMamiferos(),"\nAves: ", Ave.cantidadAves(),"\nReptiles: ", Reptil.cantidadReptiles(),"\nPeces: ", Pez.cantidadPeces(),"\nAnfibios: ", Anfibio.cantidadAnfibios)
        return resultado
    def toString(self):
        if self.zona=="none":
            retorno=("mi nombre es ",self.nombre,", tengo una edad de ",self.edad,", habito en ",self.habitat," y mi genero es ",self.genero)
            return retorno
        else:
            retorno=("mi nombre es ",self.nombre,", tengo una edad de ",self.edad,", habito en ",self.habitat," y mi genero es ",self.genero,", la zona en la que me ubico es ",self.zona,", en el ",self.zona.zoo)
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getHabitat(self):
        return self.habitat
    def getGenero(self):
        return self.genero
    def getZona(self):
        return self.zona