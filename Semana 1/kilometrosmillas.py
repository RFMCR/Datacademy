def KMaMillas():
    km=float(input("Ingresa los kilometros: "))
    print("{} km equivalen a {} millas.".format(km,km*1.609344)) 

def millasaKM():
    millas=float(input("Ingresa las millas: "))
    print("{} millas equivalen a {} KM.".format(millas,millas/1.609344)) 
    

def main():
    opcion = 0
    print ("Seleccione la opcion:")
    print ("1 -Millas a KM")
    print ("2 -KM a Millas")
    while opcion <1 or opcion>2:
        opcion = int(input())

    if opcion == 1:
        millasaKM()
    else:
        KMaMillas()


if __name__ == "__main__":
    main()