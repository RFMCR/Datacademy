def tipotriangulo():
    print("Ingrese el tamaño del lado 1")
    lado1 = float(input())
    print("Ingrese el tamaño del lado 2")
    lado2 = float(input())
    print("Ingrese el tamaño del lado 3")
    lado3 = float(input())
    if lado1 == lado2 and lado1 == lado3:
        print("Este es un triangulo Equilatero")
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print ("Este es un triangulo Escaleno")
    else:
        print ("Este es un triangulo isosceles")


def main():
    b = float(input("Ingresa la base: "))
    a = float(input("Ingresa la altura: "))
    r = (b*a)/2
    print ("El area del triangulo es: ",r)
    print ("")
    print ("Quieres saber que tipo de triangulo es? Si/no")
    respuesta = ""
    while respuesta.lower() != "si" and respuesta.lower() != "no":
        respuesta = input().lower()
    
    if respuesta == "si":
        tipotriangulo()

    


if __name__ == '__main__':
    main()