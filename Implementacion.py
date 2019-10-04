from Pila import *
from Cola import *

def main():
    numero = 8
    numeroBinario = 0
    miPila = PilaDinamica()
    miCola = ColaDinamica()
    resultado = numero
    residuo = 0
    while True:
        residuo = resultado % 2
        resultado = resultado // 2
        miCola.Insertar(residuo)
        if resultado == 0:
            break

    for x in range(0, miCola.MostrarTamCola(), 1):
        print(miCola.Quitar(), end="")
    return 0

if __name__==  '__main__':
    main()