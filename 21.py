import random
import math

def comprobar_mano_jugador(mazo):    
    if(mazo==[]):
        return 0
    else:
        return mazo[0] + comprobar_mano_jugador(mazo[1:])
    
def comprobar_mano_banca(mazo):    
    if(mazo==[]):
        return 0
    else:
        return mazo[0] + comprobar_mano_banca(mazo[1:])
        
            
def baraja(mazo,mazoBase,rnd,t):
    if(len(mazo)<=40):
        if(len(mazoBase)>=1 and t>1):
            mazo.append(mazoBase[rnd])
            mazoBase.pop(rnd)
            baraja(mazo,mazoBase,
                   math.floor(random.randrange(0,t-1)),t-1)
    return mazo

def Valor_as(mazo):
    if(mazo<=10):
        return mazo+11
    else:
        return mazo+1
                    
def jugador(baraja, mJugador,mBanca):
    print("baraja: ",baraja)
    print("Mano del Jugador: ", mJugador)    
    if(len(mJugador)<2 and len(mBanca)<2):
        jugador(baraja[2:],mJugador+[baraja[0]]+[baraja[1]],
                mBanca+[baraja[0]]+[baraja[1]])
    else:
        if(comprobar_mano_jugador(mJugador)<=21):            
            if(comprobar_mano_jugador(mJugador)==21):
                print("Ganaste")
            elif(input("Quiere una carta?  ")==('s' or 'S')):
                print(len(mJugador))
                jugador(baraja[1:],mJugador+[baraja[0]],mBanca+
                        [baraja[math.floor(random.randrange(0,40))]])                
            else:
                print("Mano del Jugador: ", mJugador)
                print(comprobar_mano_jugador(mJugador))
                print("Mano de la Banca : ", mBanca)
                print(comprobar_mano_banca(mBanca))
                if(comprobar_mano_banca(mBanca)> comprobar_mano_jugador(mJugador)
                   and comprobar_mano_banca(mBanca)<=21):
                     print("perdiste")
                elif(comprobar_mano_jugador(mJugador)>comprobar_mano_banca(mBanca)
                     and comprobar_mano_jugador(mJugador)<=21):     
                     print("Ganaste")
        else:
            print(comprobar_mano_jugador(mJugador))
            print("perdiste")


jugador(baraja([],[1,1,1,1,2,2,2,2,
                   3,3,3,3,4,4,4,4,
                   5,5,5,5,6,6,6,6,
                   7,7,7,7,8,8,8,8,
                   9,9,9,9,10,10,10,10],
        math.floor(random.randrange(0,40)),40),
        [math.floor(random.randrange(1,10)),
         math.floor(random.randrange(1,10))],
        [math.floor(random.randrange(1,10)),
         math.floor(random.randrange(1,10))])

