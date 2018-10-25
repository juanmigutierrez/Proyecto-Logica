#-*-coding: utf-8-*-

# Edgar Andrade, 2018
# Codigo para crear la formula del problema de los caballos

print ("Importando paquetes...")
from timeit import default_timer as timer
import sys
sys.path.insert(0, 'C:/Users/Recup/OneDrive/Documentos/Logica/Proyecto-Logica/Codigo/Tableaux.py')
import Tableaux as T
print ("Importados!")
# Guardo el tiempo al comenzar el procedimiento
start = timer()

# Regla 1: Debe haber exactamente tres caballos

# Creo las letras proposicionales
letrasProposicionales = []
s=""
for i in range(1, 17):
        if i < 10:
                s+="0"
        letrasProposicionales.append(s+str(i))
        s=""

# print "Letras proposicionales: ", letrasProposicionales

# Regla 1: Debe haber exactamente tres caballos
conjunciones = '' # Para ir guardando las conjunciones de trios de disyunciones de literales
inicial = True # Para inicializar la primera conjuncion
CONT=0
for p in letrasProposicionales:
    print (CONT*100/16)," % de letras creadas"
    CONT+=1
    aux1 = [x for x in letrasProposicionales if x != p] # Todas las letras excepto
    #print "aux1: ", aux1
    for q in aux1:
        #print q
        aux2 = [x for x in aux1 if x != q] # Todas las letras excepto p y q
        #print "aux2", aux2
        for r in aux2:
            aux3 = [x for x in aux2 if x != r]
            for s in aux3:
                literal = s + r + q + p + 'Y' +'Y'+'Y'
                aux4 = [x + '-' for x in aux3 if x != s]
                for k in aux4:
                    literal = k + literal + 'Y'
                #print "Literal: ", literal
                if inicial: # Inicializar la primera conjuncion
                    conjunciones = literal
                    inicial = False
                else:
                    conjunciones = literal + conjunciones + 'O'
#print "Conjunciones: ", conjunciones

# Regla 2: Ninguna reina debe poder atacar a otra
print "AGREGANDO REGLA 2"
conjunciones = '02-03-04-05-06-09-11-13-16-YYYYYYYY01>' + conjunciones + 'Y'
conjunciones = '01-03-04-05-06-07-10-12-14-YYYYYYYY02>' + conjunciones + 'Y'
conjunciones = '01-02-04-06-07-08-09-11-15-YYYYYYYY03>' + conjunciones + 'Y'
conjunciones = '01-02-03-07-08-10-12-13-16-YYYYYYYY04>' + conjunciones + 'Y'
conjunciones = '01-02-06-07-08-09-10-13-15-YYYYYYYY05>' + conjunciones + 'Y'
conjunciones = '01-02-03-05-07-08-09-10-11-14-16-YYYYYYYYYY06>' + conjunciones + 'Y'
conjunciones = '02-03-04-05-06-08-10-11-12-13-15-YYYYYYYYYY07>' + conjunciones + 'Y'
conjunciones = '03-04-05-06-07-11-12-14-16-YYYYYYYY08>' + conjunciones + 'Y'
conjunciones = '01-03-05-06-10-11-12-13-14-YYYYYYYY09>' + conjunciones + 'Y'
conjunciones = '02-04-05-06-07-09-11-12-13-14-15-YYYYYYYYYY10>' + conjunciones + 'Y'
conjunciones = '01-03-06-07-08-09-10-12-14-15-16-YYYYYYYYYY11>' + conjunciones + 'Y'
conjunciones = '02-04-07-08-09-10-11-15-16-YYYYYYYY12>' + conjunciones + 'Y'
conjunciones = '01-04-05-07-09-10-14-15-16-YYYYYYYY13>' + conjunciones + 'Y'
conjunciones = '02-06-08-09-10-11-13-15-16-YYYYYYYY14>' + conjunciones + 'Y'
conjunciones = '03-05-07-10-11-12-13-14-16-YYYYYYYY15>' + conjunciones + 'Y'
conjunciones = '01-04-06-08-11-12-13-14-15-YYYYYYYY16>' + conjunciones + 'Y'
print "REGLA 2 AGREGADA"
# Creo la formula como objeto

A1 = T.StringtoTree(conjunciones, letrasProposicionales)
#print ("Formula: ", T.Inorder(A1))

#A1 = T.StringtoTree('02-03-04-05-06-09-11-13-16-YYYYYYYY01>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A1))
#A2 = T.StringtoTree('01-03-04-05-06-07-10-12-14-YYYYYYYY02>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A2))
#A3 = T.StringtoTree('01-02-04-06-07-08-09-11-15-YYYYYYYY03>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A3))
#A4 = T.StringtoTree('01-02-03-07-08-10-12-13-16-YYYYYYYY04>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A4))
#A5 = T.StringtoTree('01-02-06-07-08-09-10-13-15-YYYYYYYY05>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A5))
#A6 = T.StringtoTree('01-02-03-05-07-08-09-10-11-14-16-YYYYYYYYYY06>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A6))
#A7 = T.StringtoTree('02-03-04-05-06-08-10-11-12-13-15-YYYYYYYYYY07>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A7))
#A8 = T.StringtoTree('03-04-05-06-07-11-12-14-16-YYYYYYYY08>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A8))
#A9 = T.StringtoTree('01-03-05-06-10-11-12-13-14-YYYYYYYY09>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A9))
#A10 = T.StringtoTree('02-04-05-06-07-09-11-12-13-14-15-YYYYYYYYYY10>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A10))
#A11 = T.StringtoTree('01-03-06-07-08-09-10-12-14-15-16-YYYYYYYYYY11>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A11))
#A12 = T.StringtoTree('02-04-07-08-09-10-11-15-16-YYYYYYYY12>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A12))
#A13 = T.StringtoTree('01-04-05-07-09-10-14-15-16-YYYYYYYY13>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A13))
#A14 = T.StringtoTree('02-06-08-09-10-11-13-15-16-YYYYYYYY14>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A14))
#A15 = T.StringtoTree('03-05-07-10-11-12-13-14-16-YYYYYYYY15>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A15))
#A16 = T.StringtoTree('01-04-06-08-11-12-13-14-15-YYYYYYYY16>', letrasProposicionales)
#print ("Formula: ", T.Inorder(A16))

lista_hojas = [[A1]] # Inicializa la lista de hojas
#lista_hojas = [[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16]] # Inicializa la lista de hojas

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

