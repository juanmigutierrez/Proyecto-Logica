import pygame
import os
import time
import random
#Utilizamos Pygame que es una libreria para hacer videojuegos, en esta libreria es posible tambien graficar y no necesariamente Tener que crear un juego.

#Clase Reina que guarda su posición
class Reina:
    def __init__(self):
        self.pos=(-120,-120)

#El tablero se creó previamente con estos parametros y pygame pero se importo la imagen por cuestiones de rendimiento
width = 480 # Ancho del tablero == height (Alto) ya que es un tablero cuadrado
board_size =4 #Tamaño del tablero en este caso 4x4
square_size =width/board_size #Tamaño de cada cuadro(simetrico con el tamaño completo del tablero)

#Creacion de las cuatro reinas(solo posición)
reina1=Reina()
reina2=Reina()
reina3=Reina()
reina4=Reina()

def inttocoord(n): #Metodo que convierte un entero n a coordenadas (x,y) en el tablero
                   # n = casilla del tablero entre 1 y 16
    if 1<=n and n<=4:
        return ((square_size*(n-1))+10,10)
    elif 5<=n and n<=8:
        return ((square_size*(n-5))+10,square_size+10)
    elif 9<=n and n<=12:
        return ((square_size*(n-9))+10,(square_size*2)+10)
    elif 13<=n and n<=16:
        return ((square_size*(n-13))+10,(square_size*3)+10)
    else:
        return ((square_size*3)+10,(square_size*3)+10)


def ponerreinas(r1,r2,r3,r4): #Metodo que modifica la posición de las reinas
    reina1.pos=inttocoord(r1)
    reina2.pos=inttocoord(r2)
    reina3.pos=inttocoord(r3)
    reina4.pos=inttocoord(r4)

def ChessBoard(): #Creacion del tablero
    pygame.init()
    Abierto=True
    flag=True
    Stringfont=pygame.font.SysFont("monospace",45)
    solucion=Stringfont.render("Solucion Correcta",15,(255,0,0))
    solucionpos=Stringfont.render("Posible Solucion",1,(255,0,0))
    
    #Se crea la ventana 480 Pixels de alto,480 Pixels de ancho
    board = pygame.display.set_mode((width,width))
    pygame.display.set_caption("Problema Reinas Miguel Vidal y David Martinez")
    
    # Dirección de la imagen para que funcione en cualquier computador
    current_path = os.path.dirname('C:\Users\dmart\Desktop\Codigo') #ADVERTENCIA : Aca va la direccion donde guardo el archivo "Proyecto-Logica\Codigo"
    resource_path = os.path.join(current_path, 'Codigo')

    #Reinas (se carga la imagen)
    reina=pygame.image.load(os.path.join(resource_path, "reina2.png")).convert_alpha()
    reina=pygame.transform.scale(reina,(100,100)) # Se escalan las imagenes para que queden centradas en sus cuadrados
    table=pygame.image.load(os.path.join(resource_path, "tablero.PNG")).convert_alpha()

    #Hilo principal del programa
    while Abierto:
        
        if flag: #Ubica las reinas en posiciones random(simulando posibles soluciones)
            ponerreinas(random.randint(1,16),random.randint(1,16),random.randint(1,16),random.randint(1,16))
            flag=False
        else:  #Ubica a las reinas en la solución correcta
            ponerreinas(3,5,12,14)
            flag=True

        #Refresca la imagen(cuestiones de animación)
        board.blit(table,(0,0))
        if flag:
            board.blit(solucion,(15,(width/2)-25))
        else:
            board.blit(solucionpos,(15,(width/2)-25))
        board.blit(reina,reina1.pos) # Codigo Que pone las reinas en su lugar
        board.blit(reina,reina2.pos)
        board.blit(reina,reina3.pos)
        board.blit(reina,reina4.pos)   
        pygame.display.flip()
        time.sleep(1)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                print "Ese ha sido el tablero con 4 reinas sin atacarse entre ellas"
                Abierto=False


ChessBoard() 
