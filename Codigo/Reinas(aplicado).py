#-*-coding: utf-8-*-

# Edgar Andrade, 2018
# Codigo para crear la formula del problema de los caballos

print ("Importando paquetes...")
from timeit import default_timer as timer
import sys
sys.path.insert(0, 'C:/Users/Recup/OneDrive/Documentos/Logica/Proyecto-Logica/Codigo/Tableaux.py')
import Tableaux as Tab
print ("Importados!")
# Guardo el tiempo al comenzar el procedimiento
start = timer()

# Regla 1: Debe haber exactamente tres caballos

# Creo las letras proposicionales
letrasProposicionales = []
for i in range(1, 17):
    letrasProposicionales.append(str(i))

# print "Letras proposicionales: ", letrasProposicionales

# Regla 1: Debe haber exactamente tres caballos
conjunciones = '' # Para ir guardando las conjunciones de trios de disyunciones de literales
inicial = True # Para inicializar la primera conjuncion

for p in letrasProposicionales:
    print p
    aux1 = [x for x in letrasProposicionales if x != p] # Todas las letras excepto
    print "aux1: ", aux1
    for q in aux1:
        print q
        aux2 = [x for x in aux1 if x != q] # Todas las letras excepto p y q
        print "aux2", aux2
        for r in aux2:
            aux3 = [x for x in aux2 if x != r]
            for s in aux3:
                literal = s + r + q + p + 'Y' + 'Y'+'Y'
                aux4 = [x + '-' for x in aux3 if x != r]
                for k in aux4:
                    literal = k + literal + 'Y'
                print "Literal: ", literal
                if inicial: # Inicializar la primera conjuncion
                    conjunciones = literal
                    inicial = False
                else:
                    conjunciones = literal + conjunciones + 'O'

        print "Conjunciones: ", conjunciones

# Regla 2: Ningun caballo debe poder atacar a otro

conjunciones = '2-3-4-5-6-9-11-13-16-YYYYYYYY1>' + conjunciones + 'Y'
conjunciones = '1-3-4-5-6-7-10-12-14-YYYYYYYY2>' + conjunciones + 'Y'
conjunciones = '1-2-4-6-7-8-9-11-15-YYYYYYYY3>' + conjunciones + 'Y'
conjunciones = '1-2-3-7-8-10-12-13-16-YYYYYYYY4>' + conjunciones + 'Y'
conjunciones = '1-2-6-7-8-9-10-13-15-YYYYYYYY5>' + conjunciones + 'Y'
conjunciones = '1-2-3-5-7-8-9-10-11-14-16-YYYYYYYY6>' + conjunciones + 'Y'
conjunciones = '2-3-4-5-6-8-10-11-12-13-15-YYYYYYYY7>' + conjunciones + 'Y'
conjunciones = '3-4-5-6-7-11-12-14-16-YYYYYYYY8>' + conjunciones + 'Y'
conjunciones = '1-3-5-6-10-11-12-13-14-YYYYYYYY9>' + conjunciones + 'Y'
conjunciones = '2-4-5-6-7-9-11-12-13-14-15-YYYYYYYY10>' + conjunciones + 'Y'
conjunciones = '1-3-6-7-8-9-10-12-14-15-16-YYYYYYYY11>' + conjunciones + 'Y'
conjunciones = '2-4-7-8-9-10-11-15-16-YYYYYYYY12>' + conjunciones + 'Y'
conjunciones = '1-4-5-7-9-10-14-15-16-YYYYYYYY13>' + conjunciones + 'Y'
conjunciones = '2-6-8-9-10-11-13-15-16-YYYYYYYY14>' + conjunciones + 'Y'
conjunciones = '3-5-7-10-11-12-13-14-16-YYYYYYYY15>' + conjunciones + 'Y'
conjunciones = '1-4-6-8-11-12-13-14-15-YYYYYYYY16>' + conjunciones + 'Y'

# Creo la formula como objeto
A = T.StringtoTree(conjunciones, letrasProposicionales)
print ("Formula: ", T.Inorder(A))

lista_hojas = [[A]] # Inicializa la lista de hojas

OK = ('') # El tableau regresa Satisfacible o Insatisfacible
interpretaciones = [] # lista de lista de literales que hacen verdadera lista_hojas

OK, INTS = T.Tableaux(lista_hojas, letrasProposicionales)

print ("Tableau terminado!")
# Guardo el tiempo al terminar el procedimiento
end = timer()
print (u"El procedimiento demoró: ", end - start)

if OK == ('Satisfacible'):
    if len(INTS) == 0:
        print (u"Error: la lista de interpretaciones está vacía")
    else:
        print ("Guardando interpretaciones en archivo...")
        import csv
        archivo = ('tableros_automatico.csv')
        with open(archivo, 'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(INTS)

        print ("Interpretaciones guardadas  en " + archivo)

        import visualizacion as V
        contador = 1
        for i in INTS:
            print ("Trabajando con literales: ", i)
            V.dibujar_tablero(i,contador)
            contador += 1

print ("FIN")

