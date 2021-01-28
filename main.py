from random import randrange
def write_menu():
    print("--------------------")
    print("BLACKJACK \n1. Modo fácil \n2. Modo normal \n0. Salir")
    print("--------------------")
    option = get_option("Escoja una opcion: ")
    if (option == 1):
        play(option)
    elif (option == 2):
        play(option)
    elif (option == 0):
        print(exit(0))
    else:
        print("Error! Seleccione una opción válida")
        write_menu()

def get_option(msg):
    try:
        op = int(input(msg))
    except ValueError:
        op = None
    finally:
        return op

def play(option):
    croupier = 0
    i=0 #Croupier iterations
    player=0
    j=0 #Player iterations
    while(croupier<15):
        croupier+=randrange(12)
        i+=1
    print("--------------------")
    if(option==1):
        print("La puntuación del croupier es: ",croupier)
    player+=randrange(12)
    j+=1
    print("Su puntuación inicial es: ",player)
    print("--------------------")
    while True:
        if turn():
            player += randrange(12)
            j += 1
            print("Su puntuación es: ",player)
            print("--------------------")
        else:
            break
    display_info(croupier,i,player,j)
    if(croupier>=22 and player<=22): #Croupier >21
            victory()
    elif(croupier>=22 and player>=22): #Both >21
        if(player<croupier):
            victory()
        else:
            defeat()
    elif(croupier<=22 and player>=22): #Player >21
        defeat()
    elif(croupier<=22 and player<=22): #Croupier & Player <21
        if(croupier>player):
            defeat()
        else:
            victory()
    elif(croupier==player):
            if(i<j):
                defeat()
            else:
                victory()
    else:
        print(" Fatal error")

    print(" Final del juego")
    print(" Cerrando programa...")

def display_info(croupier,i,player,j):
    print("*-------------------------*")
    print("|INFORMACIÓN DE LA PARTIDA|")
    print("*-------------------------*")
    print("|-----------------------------------|")
    print(" Puntuación del croupier: ", croupier)
    print(" Intentos del croupier: ", i)
    print(" Puntuación del jugador: ", player)
    print(" Intentos del croupier: ", j)
    print("|-----------------------------------|")
    print(" Calculando resultados...")
    print("|-----------------------------------|")
def turn():
    print("¿Seguir jugando? \n1. Sí\n2. No")
    print("--------------------")
    option=get_option("Escoja una opción: ")
    if(option==1):
        return True
    elif(option==2):
        return False
    else:
        print("Elija una opción válida!")
def victory():
    print("*--------*")
    print("|VICTORIA|")
    print("*--------*")
def defeat():
        print("*-------*")
        print("|DERROTA|")
        print("*-------*")

if __name__ == '__main__':
    write_menu()
