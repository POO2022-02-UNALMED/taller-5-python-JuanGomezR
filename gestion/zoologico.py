class Zoologico:
    def __init__(self, nombre, ubicacion, zonas=[]):
        self.nombre=nombre
        self.ubicacion=ubicacion
        self.zonas=zonas
    def agregarZonas(self, zona):
        self.zonas.append(zona)
    def cantidadTotalAnimales(self):
        total=0
        for i in self.zonas:
            from gestion.zona import Zona
            total+=i.cantidadAnimales()
        return total
    def getZona(self):
        return self.zonas
    def getNombre(self):
        return self.nombre