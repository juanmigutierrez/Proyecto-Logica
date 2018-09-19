import pygame

#Utilizamos Pygame que es una libreria para hacer videojuegos, en esta libreria es posible tambien graficar y no necesariamente Tener que crear un juego.

width = 480
height = 480
color_cell = [(253, 235, 208), (214, 137, 16)]
board_size =4
square_size =width/board_size


def ChessBoard(r1,r2,r3,r4): # n es el numero de cuadros x cuadros , EJEMPLO  si n = 4, es un tablero 4x4
    pygame.init()
    
    #se crea la ventana 480 Pixels de alto,480 Pixels de ancho
    board = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Problema Reinas Miguel Vidal y David Martinez")
    
    #Reinas
    reina_negra=pygame.image.load("reinacasnegra.png").convert_alpha()
    reina_blanca=pygame.image.load("reinacasblanca.png").convert_alpha()
    
    #se crea el tablero
    for filas in range(board_size):           # Dibuja cada fila en el ChessBoard
        c_indx = filas % 2           # Alterna de color
        for columnas in range(board_size):       # Va pasando por las columnas
              cuadrado = (columnas*square_size, filas*square_size ,square_size, square_size)
              board.fill(color_cell[c_indx], cuadrado)
              c_indx = (c_indx + 1) % 2
   
    board.blit(reina_blanca,inttocoord(r1))
    board.blit(reina_blanca,inttocoord(r2))
    board.blit(reina_blanca,inttocoord(r3))
    board.blit(reina_blanca,inttocoord(r4))
        
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()

def inttocoord(n):
    if n==1:
        return (10,10)
    elif n==2:
        return (square_size+10,10)
    elif n==3:
        return ((square_size*2)+10,10)
    elif n==4:
        return ((square_size*3)+10,10)
    elif n==5:
        return ((square_size*0)+10,(square_size*1)+10)
    elif n==6:
        return ((square_size*1)+10,(square_size*1)+10)
    elif n==7:
        return ((square_size*2)+10,(square_size*1)+10)
    elif n==8:
        return ((square_size*3)+10,(square_size*1)+10)
    elif n==9:
        return ((square_size*0)+10,(square_size*2)+10)
    elif n==10:
        return ((square_size*1)+10,(square_size*2)+10)
    elif n==11:
        return ((square_size*2)+10,(square_size*2)+10)
    elif n==12:
        return ((square_size*3)+10,(square_size*2)+10)
    elif n==13:
        return ((square_size*0)+10,(square_size*3)+10)
    elif n==14:
        return ((square_size*1)+10,(square_size*3)+10)
    elif n==15:
        return ((square_size*2)+10,(square_size*3)+10)
    else:
        return ((square_size*3)+10,(square_size*3)+10)
ChessBoard(5,9,7,1) 
