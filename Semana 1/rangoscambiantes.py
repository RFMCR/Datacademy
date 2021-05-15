def main():
    print("Ingrese el número menor")
    menor = int(input())
    print("Ingrese el número mayor")
    mayor = int(input())
    acerto = False
    while acerto == False:
        print("Ingrese otro número")
        num = int(input())
        if menor <= num <= mayor:
            print("El número esta dentro del rango")
            acerto = True
        else:
            print("El número está fuera del rango")

if __name__ == '__main__':
    main()