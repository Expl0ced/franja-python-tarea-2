# Ejercicio 2: Escribir una función que calcule el área de un círculo y 
# otra que calcule el volumen de un cilindro usando la primera función.
import math

def circulo(pi, radio):
    radio=radio**2
    return pi*radio

def cilindro(pi, radio, h):
    return circulo(pi, radio)*h


def main():
    radio=float(input("ingrese el radio para el circulo y el cilindro: "))
    h=float(input("ingrese la altura del cilindro: "))
    pi=round(math.pi, 2)
    print("el area del circulo es: "+str(circulo(pi,radio))+ " , el radio del cilindro es: "+ str(cilindro(pi, radio, h)))

25
if __name__ == '__main__':
    main()