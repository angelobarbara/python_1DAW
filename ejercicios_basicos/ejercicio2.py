def main():
    a = int(input("Introduzca un numero entero: "))
    print("Introduzca un numero mayor que",a,": ")
    b = int(input())
    while b < a:
        print("Introduzca un numero mayor que",a,": ")
        b = int(input())
    print ("Los numeros introducidos son:",a,"y",b)


main()