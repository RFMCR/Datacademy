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


def ganador(j1,j2):
    if (j1.lower() == "piedra" and j2.lower()== "tijera") or (j1.lower() == "papel" and j2.lower()== "piedra") or (j1.lower() == "tijera" and j2.lower()== "papel"):
        return 1
    elif (j2.lower() == "piedra" and j1.lower()== "tijera") or (j2.lower() == "papel" and j1.lower()== "piedra") or (j2.lower() == "tijera" and j1.lower()== "papel"):
        return 2    
    else:
        return 0


def main():
    recordj1 = 0
    recordj2 = 0
    recordempates = 0
    juegos = 1
    intentos = 1
    resultado = 0
    denuevo = ""

    while intentos <=juegos:
        j1=""
        j2=""
        while j1.lower() != "piedra" and j1.lower() != "papel" and j1.lower() != "tijera":
            clear()
            j1 = input("Jugador 1, escoge piedra, papel o tijera ").lower()

        while j2.lower() != "piedra" and j2.lower() != "papel" and j2.lower() != "tijera":
            clear()
            j2 = input("Jugador 2, escoge piedra, papel o tijera ").lower()

        resultado = ganador(j1,j2)
        
        if resultado == 1:
            print ("Gano el Jugador 1")
            recordj1 +=1
        elif resultado == 2:
            print ("Gano el Jugador 2")
            recordj2 +=1
        else:
            print ("Empate")
            recordempates +=1

        while denuevo != "si" and denuevo != "no":
            denuevo = input("De nuevo? si/no  ").lower()

        if denuevo == 'si':
            juegos+=1
            denuevo = ""
        else:
            denuevo = ""
            print ("Se jugaron {} juegos. El jugador 1 ganó {}, el jugador 2 ganó {} y se empataron {}".format(juegos,recordj1,recordj2,recordempates))

        intentos+=1


if __name__ == '__main__':
    main()