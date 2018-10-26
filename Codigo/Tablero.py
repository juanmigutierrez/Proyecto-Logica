import pygame
import os,sys
import time
import csv
import math
from inspect import getsourcefile

#Utilizamos Pygame que es una libreria para hacer videojuegos, en esta libreria es posible tambien graficar y no necesariamente Tener que crear un juego.

width = 600
height = 600
color_cell = [(253, 235, 208), (214, 137, 16)]
background = [] # Se crea una memoria del tablero sin fichas (x,y) donde x = color y=cuadrado coloreado, este sera guardado para cada vez que se mueva ficha

def ChessBoard(lista): 
    board_size=int(math.sqrt(len(lista)))
    square_size =width//board_size # El // es para que quede entero y en el scale no ponga problemas cada vez que se cambia
    #se crea la ventana 480 Pixels de alto,480 Pixels de ancho
    board = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Problema Reinas Miguel Vidal y David Martinez")
    
    #se crea el tablero
    for filas in range(board_size):           # Dibuja cada fila en el ChessBoard
        c_indx = filas % 2           # Alterna de color
        for columnas in range(board_size):       # Va pasando por las columnas
              cuadrado = (columnas*square_size, filas*square_size ,square_size, square_size)
              board.fill(color_cell[c_indx], cuadrado)
              background.append((color_cell[c_indx],cuadrado)) # Se agrega cada cuadro a background
              c_indx = (c_indx + 1) % 2
    return board


def poner_reina(n,board_size):
    square_size =width//board_size
    lista = []
    for i in range(board_size+1):
        lista.append(i*board_size)
    for i in range(len(lista)): #columna = n-lista[i]-1 , fila = lista[i]
        if lista[i]<=n and n<=lista[i+1]:
            return((n-lista[i]-1)*square_size, i*square_size ,square_size, square_size)


def pos_reina(lista,board,n):  # Codigo Basico sin nada
    board_size=int(math.sqrt(len(lista)))
    square_size =width//board_size
       #Reinas
    reina=pygame.image.load(os.path.join("reina.png")).convert_alpha()
    reina=pygame.transform.scale(reina,(square_size,square_size)) # Se escalan las imagenes para que queden centradas en sus cuadrados
    for reina1 in lista:
         if '-' not in reina1:
            board.blit(reina,poner_reina(int(reina1),board_size))
    pygame.display.update()
    pygame.time.delay(800)
    pygame.image.save(board, 'Respuesta/Tablero'+str(n)+'.png') #ADVERTENCIA : Aca va la direccion donde guardo el archivo "Proyecto-Logica\Codigo"
    return board

def llenar(reina):
    board.fill(background[reina-1][0],background[reina-1][1])
    

def pos_pos_reina(lista1,lista2,board,n):
    board_size=int(math.sqrt(len(lista2)))
    square_size =width//board_size
    for reina in lista1:
        if '-' not in reina:
            llenar(int(reina))
    pygame.display.update()
    pygame.time.delay(100)

    #Reinas
    reina=pygame.image.load(os.path.join(resource_path, "reina.png")).convert_alpha()
    reina=pygame.transform.scale(reina,(square_size,square_size)) # Se escalan las imagenes para que queden centradas en sus cuadrados
    for reina1 in lista2:
        if '-' not in reina1:
            board.blit(reina,poner_reina(int(reina1),board_size))
    pygame.display.update()
    pygame.time.delay(100)
    pygame.image.save(board, "SOL/"'Tablero'+str(n)+'.png') #ADVERTENCIA : Aca va la direccion donde guardo el archivo "Proyecto-Logica\Codigo"
    return board

tablerovacio = ['-1','-2','-3','-4','-5','-6','-7','-8','-9','-10','-11','-12','-13','-14','-15','-16'] 
def dibujar(listadelistas):
    pygame.init()
    Salir=False
    contador=0
    for i in listadelistas:
        board = ChessBoard(i)
        board = pos_reina(i,board,contador)
        contador+=1
        pygame.display.flip()
    while not Salir:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                Salir=True
#prueba=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16']
#lista=[prueba,prueba,prueba]
#dibujar(lista)
