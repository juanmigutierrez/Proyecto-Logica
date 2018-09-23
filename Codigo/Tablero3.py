import pygame
import os
import time
#Utilizamos Pygame que es una libreria para hacer videojuegos, en esta libreria es posible tambien graficar y no necesariamente Tener que crear un juego.

width = 600
height = 600
color_cell = [(253, 235, 208), (214, 137, 16)]
board_size =4 # IMPORTANTE : Cambiar esta variable para cambiar tablero
square_size =width//board_size # El // es para que quede entero y en el scale no ponga problemas cada vez que se cambia
background = [] # Se crea una memoria del tablero sin fichas (x,y) donde x = color y=cuadrado coloreado, este sera guardado para cada vez que se mueva ficha

def ChessBoard(lista): 
    board_size=len(lista)
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
    lista = []
    for i in range(board_size+1):
        lista.append(i*board_size)
    for i in range(len(lista)): #columna = n-lista[i]-1 , fila = lista[i]
        if lista[i]<=n and n<=lista[i+1]:
            return((n-lista[i]-1)*square_size, i*square_size ,square_size, square_size)


def pos_reina(lista,board):  # Codigo Basico sin nada
    # Direccion de la imagen para que funcione en cualquier computador
    current_path = os.path.dirname('C:/Users/Recup/source/repos/Proyecto-Logica/Codigo') #ADVERTENCIA : Aca va la direccion donde guardo el archivo "Proyecto-Logica\Codigo"
    resource_path = os.path.join(current_path, 'Codigo')

    #Reinas
    reina=pygame.image.load(os.path.join(resource_path, "reina.png")).convert_alpha()
    reina=pygame.transform.scale(reina,(square_size,square_size)) # Se escalan las imagenes para que queden centradas en sus cuadrados
    board_size = len(lista)
    for reina1 in lista:
        board.blit(reina,poner_reina(reina1,board_size))
    pygame.display.update()
    pygame.time.delay(100)
    return board

def llenar(reina):
    board.fill(background[reina-1][0],background[reina-1][1])
    

def pos_pos_reina(lista1,lista2,board):
    # Direccion de la imagen para que funcione en cualquier computador
    current_path = os.path.dirname('C:/Users/Recup/source/repos/Proyecto-Logica/Codigo') #ADVERTENCIA : Aca va la direccion donde guardo el archivo "Proyecto-Logica\Codigo"
    resource_path = os.path.join(current_path, 'Codigo')
    for reina in lista1:
        llenar(reina)
    pygame.display.update()
    pygame.time.delay(100)

    #Reinas
    reina=pygame.image.load(os.path.join(resource_path, "reina.png")).convert_alpha()
    reina=pygame.transform.scale(reina,(square_size,square_size)) # Se escalan las imagenes para que queden centradas en sus cuadrados
    board_size = len(lista2)
    for reina1 in lista2:
        board.blit(reina,poner_reina(reina1,board_size))
    pygame.display.update()
    pygame.time.delay(100)
    return board
   

# Aca viene el juego

pygame.init()
Salir=False

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

board = ChessBoard(lista1)
board = pos_reina(lista1,board)
board = pos_pos_reina(lista1,lista2,board)

pygame.display.flip()
while not Salir:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            Salir=True






# Codigo EXTRA POR SI LAS MOSCAS
# Direccion de la imagen para que funcione en cualquier computador
current_path = os.path.dirname('C:/Users/Recup/source/repos/Proyecto-Logica/Codigo') #ADVERTENCIA : Aca va la direccion donde guardo el archivo "Proyecto-Logica\Codigo"
resource_path = os.path.join(current_path, 'Codigo')

#Reinas
reina=pygame.image.load(os.path.join(resource_path, "reina.png")).convert_alpha()
reina=pygame.transform.scale(reina,(120,120)) # Se escalan las imagenes para que queden centradas en sus cuadrados
board.blit(reina,(240.0, 0.0, 120.0, 120.0))
