import pygame
import time

#Utilizamos Pygame que es una libreria para hacer videojuegos, en esta libreria es posible tambien graficar y no necesariamente Tener que crear un juego.

def ChessBoard(n): # n es el numero de cuadros x cuadros , EJEMPLO  si n = 4, es un tablero 4x4

    pygame.init()
    colores = [(253, 235, 208), (214, 137, 16)]    # Esta en codigo RGB aca ponemos los codigos de naranja claro y naranja-cafe
    Pixeles = 480           # Pixeles * Pixeles
    lcuadrado = Pixeles // n    # Largo de cada cuadrado del ChessBoard , esta division es entera ejemplo 5//2 = 2
    Pixeles = n * lcuadrado     # Ajusta para meter los cuadrados bien, en esencia deberia ser igual a 480

    # Crea el programa con (altura,ancho) con su respectiva ventana
    surface = pygame.display.set_mode((Pixeles, Pixeles))

    for fil in range(n):           # Dibuja cada fila en el ChessBoard
            c_indx = fil % 2           # Alterna de color
            for col in range(n):       # Va pasando por las columnas
                cuadrado = (col*lcuadrado, fil*lcuadrado ,lcuadrado, lcuadrado)
                surface.fill(colores[c_indx], cuadrado)
                # Cambia el color para el proximo cuadrado
                c_indx = (c_indx + 1) % 2
    pygame.display.flip()
    os.system("pause")
    pygame.quit()
    


ChessBoard(4) 

