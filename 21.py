import random
def mazo():
    return [(numero,pinta) for numero in [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] for pinta in ['♥','♦','♣','♥']]
def valorDe(carta,valor):
    if (carta[0]==2):
        return 2
    if (carta[0]==3):
        return 3
    if (carta[0]==4):
        return 4
    if (carta[0]==5):
        return 5
    if (carta[0]==6):
        return 6
    if (carta[0]==7):
        return 7
    if (carta[0]==8):
        return 8
    if (carta[0]==9):
        return 9
    if (carta[0]==10):
        return 10
    if (carta[0]=='J'):
        return 10
    if (carta[0]=='Q'):
        return 10
    if (carta[0]=='K'):
        return 10
    if (carta[0]=='A'):
        if(valor>10):
            return 1
        else:
            return 11
def obtenerValor(mano):
    return obtenerValorOrden(sorted(mano, key=str))
def obtenerValorOrden(mano):
    if (mano==[]):
        return 0
    else:
        valor=obtenerValor(mano[1:])
        return valor+valorDe(mano[0],valor)
def tomarCarta(mazo):
    if (mazo!=[]):
        return [mazo.pop(random.randrange(len(mazo)))]
    else:
        return []
def jugar(mazo,manoJugador,manoPc):
    print("Tienes las cartas: ",manoJugador)
    print("La banca tiene la carta: ",manoPc[0])
    print("La suma de tus cartas es: ",obtenerValor(manoJugador))     
    if(obtenerValor(manoJugador)<21):
        if (input("¿Desea tomar otra carta?(s/n)")==('s' or 'S')):
            jugar(mazo,manoJugador+tomarCarta(mazo),manoPc)
        else:
            Juego(mazo,manoJugador,manoPc)
    else:
        Juego(mazo,manoJugador,manoPc)
def Juego(mazo,manoJugador,manoPc):
    print("La banca tiene las cartas: ",manoPc)
    print("La suma de las cartas de la banca es: ",obtenerValor(manoPc))
    if(obtenerValor(manoJugador)<=21):
        if(obtenerValor(manoPc)>21):       
            print("GANASTE con: ",manoJugador)
        elif(obtenerValor(manoPc)>=obtenerValor(manoJugador)):
            print("PERDISTE")
        else:
            Juego(mazo,manoJugador,manoPc+tomarCarta(mazo))
    else:
        print("PERDISTE")            
def iniciar(mazo):
    jugar(mazo,tomarCarta(mazo)+tomarCarta(mazo),tomarCarta(mazo)+tomarCarta(mazo))
iniciar(mazo())
