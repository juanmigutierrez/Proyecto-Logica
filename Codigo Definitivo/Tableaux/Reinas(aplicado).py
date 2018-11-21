#-*-coding: utf-8-*-

# Miguel Vidal y David Martinez, 2018
# Codigo para solucionar problema de reinas

print ("Importando paquetes...")
from timeit import default_timer as timer
import Tableaux as T
print ("Importados!")
# Guardo el tiempo al comenzar el procedimiento
start = timer()

# Creo las letras proposicionales
letrasProposicionales = []
s=""
for i in range(1, 17):
        if i < 10:
                s+="0"
        letrasProposicionales.append(s+str(i))
        s=""

# print "Letras proposicionales: ", letrasProposicionales

# Regla 1: Debe haber exactamente cuatro reinas por tablero
conjunciones = '' # Para ir guardando las conjunciones de grupos de disyunciones de literales
inicial = True # Para inicializar la primera conjuncion
CONT=0
print "Agregando regla 1 (Solo 4 Reinas Por Tablero)"
for p in letrasProposicionales:
    break
    print (CONT*100/16),"% De Regla 1 Creado"
    CONT+=1
    aux1 = [x for x in letrasProposicionales if x != p] # Todas las letras excepto p
    #print "aux1: ", aux1
    for q in aux1:
        #print q
        aux2 = [x for x in aux1 if x != q] # Todas las letras excepto p y q
        #print "aux2", aux2
        for r in aux2:
            aux3 = [x for x in aux2 if x != r]#Todas las letras excepto p y q y r
            for s in aux3:
                literal = s + r + q + p + 'Y' +'Y'+'Y'
                aux4 = [x + '-' for x in aux3 if x != s]#Todas las letras excepto p y q y r y s
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
print "Agregando Regla 2 (Ninguna Reina Se Ataca)"
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
print "Regla 1 Y 2 Juntas Como Una Sola Formula"

print "Creando Formula Para Iniciar En Tableaux"
print "Formula Demasiado Larga Puede Tardar Unos Segundos"
# Creo la formula como objeto

#A1 = T.StringtoTree(conjunciones, letrasProposicionales)
#print ("Formula: ", T.Inorder(A1))(OJO NO SE PUEDE IMPRIMIR FORMULA DEMASIADO GRANDE,ERROR DE MEMORIA PARA RECURSION)
print "Iniciaremos El Tableaux"

A1 = T.StringtoTree('0203-04-05-06-0911-13-16-01-07-0812-14-1510-YYYYYYYYYYYYYYY', letrasProposicionales) #Prueba muy corta para comprobar
#print ("Formula: ", T.Inorder(Prueba))

lista_hojas = [[A1]] # Inicializa la lista de hojas

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

        import Tablero as V
        print ("Dibujando su tablero: ")
        V.dibujar(INTS)

print ("FIN")

