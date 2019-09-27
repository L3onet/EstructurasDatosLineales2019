from Pila import *

def main():
    numero = 8
    numeroBinario = 0
    miPila = PilaDinamica()
    resultado = numero
    residuo = 0
    while True:
        residuo = resultado % 8
        resultado = resultado // 8
        miPila.Insertar(residuo)
        if resultado == 0:
            break

    for x in range(0, miPila.tamPila(), 1):
        print(miPila.Quitar(), end="")
    return 0

if __name__==  '__main__':
    main()