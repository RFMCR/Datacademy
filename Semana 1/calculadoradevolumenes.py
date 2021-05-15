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
        print("Seleccione el volumen a calcular:")
        print("1. Cilindro")
        print("2. Cono")
        print("3. Cubo")
        print("4. Piramide")
        print("5. Esfera")
        
        opcion = int(input())
    
    if opcion == 1:
        radio = float(input("Ingrese el radio: "))
        altura = float(input("Ingrese la altura: "))
        volumen = (math.pi * (radio **2) * altura)
        print("El volumen del cilindro es: {}".format(volumen))
    elif opcion == 2:
        radio = float(input("Ingrese el radio: "))
        altura = float(input("Ingrese la altura: "))
        volumen = (math.pi * (radio **2) * altura)/3
        print("El volumen del como es: {}".format(volumen))
    elif opcion == 3:
        arista = float(input("Ingrese la arista: "))
        volumen = arista ** 3
        print("El volumen del Cubo es: {}".format(volumen))
    elif opcion == 4:
        lado = float(input("Ingrese el lado: "))
        altura = float(input("Ingrese la altura: "))
        volumen = (altura * (lado**2))/3
        print("El volumen de la piramide  es: {}".format(volumen))
    elif opcion == 5:
        radio = float(input("Ingrese el radio: "))
        area = (4 * math.pi * (radio ** 3)) / 3
        print("El area del Cuadrado es: {}".format(area))
    
if __name__ == '__main__':
    main()

#http://www.calcularelvolumen.com/