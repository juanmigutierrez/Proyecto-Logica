import pygame

#Utilizamos Pygame que es una libreria para hacer videojuegos, en esta libreria es posible tambien graficar y no necesariamente Tener que crear un juego.

width = 480
height = 480
color_cell = [(253, 235, 208), (214, 137, 16)]
board_size =4
square_size =width/board_size


def ChessBoard(): # n es el numero de cuadros x cuadros , EJEMPLO  si n = 4, es un tablero 4x4
    pygame.init()
    
    #se crea la ventana 480 Pixels de alto,480 Pixels de ancho
    board = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Problema Reinas Miguel Vidal y David Martinez")
    
    #Reinas
    reina_blanca=pygame.image.load("reinacasnegra.png").convert_alpha()
    reina_negra=pygame.image.load("reinacasblanca.png").convert_alpha()
    
    #se crea el tablero
    for filas in range(board_size):           # Dibuja cada fila en el ChessBoard
        c_indx = filas % 2           # Alterna de color
        for columnas in range(board_size):       # Va pasando por las columnas
              cuadrado = (columnas*square_size, filas*square_size ,square_size, square_size)
              board.fill(color_cell[c_indx], cuadrado)
              c_indx = (c_indx + 1) % 2
    board.blit(reina_blanca,(15,15))


    
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()

ChessBoard() 
