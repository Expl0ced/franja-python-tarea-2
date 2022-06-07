# Ejercicio 1: Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase. 

def main():
    frase=input("ingrese una frase: ")
    letra=input("escoja una letra para contar: ")
    rep=str(frase.count(letra))
    print("la letra " + letra + " se repite "+ rep + " veces")


if __name__ == "__main__":
    main()