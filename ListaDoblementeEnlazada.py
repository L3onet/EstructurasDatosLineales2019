#Clase Nodo con dos punteros
class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def vacia(self):
        return self.primero == None

    def agregarFinal(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.tamanio += 1

    def agregarInicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.tamanio += 1

    def recorrerInicio(self):
        aux = self.primero
        while aux:
            print(aux.dato, end=" -> ")
            aux = aux.siguiente

    def recorrerFin(self):
        aux = self.ultimo
        while aux:
            print(aux.dato, end=" -> ")
            aux = aux.anterior

    def eliminarInicio(self):
        if self.vacia():
            print("Esta vacia")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.tamanio = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.tamanio -= 1

    def eliminarFinal(self):
        if self.vacia():
            print("Esta vacia")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.tamanio = 0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.tamanio -= 1


lista = ListaDoblementeEnlazada()
lista.agregarInicio(12)
lista.agregarFinal(24)
lista.agregarFinal(36)
lista.recorrerFin()
print("")
print("=============")
lista.recorrerInicio()
