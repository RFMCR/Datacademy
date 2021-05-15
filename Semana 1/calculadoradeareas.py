import math 
# import only system from os
from os import system, name

# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

        

def main ():
    opcion = 0
    while opcion<1 or opcion>9:
        clear()
        print("Seleccione el area a calcular:")
        print("1. Cilindro")
        print("2. Rectangulo")
        print("3. Triangulo")
        print("4. Trapecio")
        print("5. Cuadrado")
        print("6. Circulo")
        print("7. Hexagono")
        print("8. Cono")
        print("9. Cubo")
        
        opcion = int(input())
    
    if opcion == 1:
        radio = float(input("Ingrese el radio: "))
        altura = float(input("Ingrese la altura: "))
        area = 2 * math.pi * radio * (radio + altura)
        print("El area del cilindro es: {}".format(area))
    elif opcion == 2:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area = base * altura
        print("El area del Rectangulo es: {}".format(area))
    elif opcion == 3:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area = (base * altura) /2
        print("El area del Triangulo es: {}".format(area))
    elif opcion == 4:
        basemenor = float(input("Ingrese la base menor: "))
        basemayor = float(input("Ingrese la base mayor: "))
        altura = float(input("Ingrese la altura: "))
        area = ((basemayor + basemenor) /2 ) * altura
        print("El area del Trapecio  es: {}".format(area))
    elif opcion == 5:
        altura = float(input("Ingrese el lado: "))
        area = altura * altura
        print("El area del Cuadrado es: {}".format(area))
    elif opcion == 6:
        radio = float(input("Ingrese el radio: "))
        area = (radio ** 2) * math.pi
        print("El area del circulo es: {}".format(area))
    elif opcion == 7:
        altura = float(input("Ingrese el lado: "))
        perimetro = altura  * 6
        radians = (360/6)/2 * math.pi / 180
        tangente = math.tan(radians) 
        apotema = (altura / (2 * tangente))
        area = (perimetro * apotema) / 2
        print("El area del Hexagono  es: {}".format(area))
    elif opcion == 8:
        radio = float(input("Ingrese el radio: "))
        generatriz = float(input("Ingrese la generatriz: "))
        area1 = math.pi * radio * generatriz
        area2 = math.pi * radio * (generatriz + radio)
        print("La superficie Lateral del cono es: {}".format(area1))
        print("La superficie del cono es: {}".format(area2))
    elif opcion == 9:
        altura = float(input("Ingrese el lado: "))
        area = (altura ** 2) * 6
        print("El area del cubo  es: {}".format(area))

if __name__ == '__main__':
    main()

#http://www.calculararea.com/