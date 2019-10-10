class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaCircularDobleEnlazada():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def Vacia(self):
        if self.primero == None:
            return True
        else:
            return False

    def AgregarInicio(self, dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unir_nodos()

    def AgregarFinal(self, dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.__unir_nodos()

    def __unir_nodos(self):
        if self.primero != None:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero

    def RecorrerInicioFin(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def RecorrerFinInicio(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior
            if aux == self.ultimo:
                break

    def EliminarInicio(self):
        if self.Vacia():
            print("Esta vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
        self.__unir_nodos()

    def EliminarUltimo(self):
        if self.Vacia():
            print("Esta vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
        self.__unir_nodos()

    def Buscar(self, dato):
        aux = self.primero
        while aux:
            if aux.dato == dato:
                return True
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return False

lista = ListaCircularDobleEnlazada()
lista.AgregarFinal(12)
lista.AgregarFinal(13)
lista.AgregarFinal(14)
lista.AgregarFinal(15)
lista.RecorrerInicioFin()
print("============")
lista.EliminarInicio()
lista.EliminarUltimo()
lista.RecorrerFinInicio()