# Ejercicio 3: Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática
# el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $3.500 y si es mayor de 18 años, $8.000.

def main():
    entrada={
        '>4 años': 'el valor de la entrada es gratis',
        '4 a 18 años': 'el valor de la entrada es $3.500',
        '<18 años': 'el valor de la entrada es $8.000'
    }
    edad=int(input("ingrese la edad del cliente: "))
    if edad<4:
        print(entrada['>4 años'])
    elif edad>4 and edad<18:
        print(entrada['4 a 18 años'])
    elif edad>18:
        print(entrada['<18 años'])
    else:
        print("bro?")


if __name__ == '__main__':
    main()