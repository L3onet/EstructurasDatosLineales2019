# Implementación de una pila estática
# TAD. Tipo de dato abstracto

class PilaEstatica:
    __tamPila = int(0)
    __listaPila = []
    __cima = 0

    def __init__(self, tamPila):
        self.__tamPila = tamPila - 1
        self.__cima = -1

    def PilaLlena(self):
        if self.__cima == self.__tamPila:
            return True
        else:
            return False

    def Insertar(self, elemento):
        if self.PilaLlena():
            return  False
        else:
            self.__cima += 1
            self.__listaPila.insert(self.__cima, elemento)
            return True

    def PilaVacia(self):
        if self.__cima == -1:
            return True
        else:
            return False

    def Quitar(self):
        if self.PilaVacia():
            return False
        else:
            elemento = self.__listaPila.pop()
            self.__cima -= 1
            return elemento

    def limpiarPila(self):
        self.__listaPila.clear()

    def cimaPila(self):
        return self.__listaPila[self.__cima]

    def tamPila(self):
        return len(self.__listaPila)

#Implementación de una pila dinámica

class PilaDinamica:
    __listaPila = []

    def __init__(self):
        self.__listaPila = []

    def Insertar(self, elemento):
        self.__listaPila.append(elemento)

    def PilaVacia(self):
        if len(self.__listaPila) == 0:
            return True
        else:
            return False

    def Quitar(self):
        if self.PilaVacia():
            return False
        else:
            elemento = self.__listaPila.pop()
            return elemento

    def limpiarPila(self):
        self.__listaPila.clear()

    def tamPila(self):
        return len(self.__listaPila)