#from gestion.zona import Zona

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
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        resultado=("Mamiferos: ",Mamifero.cantidadMamiferos(),"\nAves: ", Ave.cantidadAves(),"\nReptiles: ", Reptil.cantidadReptiles(),"\nPeces: ", Pez.cantidadPeces(),"\nAnfibios: ", Anfibio.cantidadAnfibios)
        for i in resultado:
                retorno+=str(i)
        return resultado
    def toString(self):
        if self.zona=="none":
            retorno=""
            string=("mi nombre es ",self.nombre,", tengo una edad de ",self.edad,", habito en ",self.habitat," y mi genero es ",self.genero)
            for i in string:
                retorno+=str(i)
            return retorno
        else:
            retorno=""
            string=("mi nombre es ",self.nombre,", tengo una edad de ",self.edad,", habito en ",self.habitat," y mi genero es ",self.genero,", la zona en la que me ubico es ",self.zona,", en el ",self.zona.zoo)
            for i in string:
                retorno+=str(i)
            return retorno
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