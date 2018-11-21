

# Miguel Vidal y David Martinez, 2018
# Codigo para solucionar problema de reinas

print ("Importando paquetes...")
from timeit import default_timer as timer
import FormaClausal as FORM
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
print("Agregando regla 1 (Solo 4 Reinas Por Tablero)")
for p in letrasProposicionales:
    break
    print ((CONT*100/16),"% De Regla 1 Creado")
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
print ("Agregando Regla 2 (Ninguna Reina Se Ataca)")
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
print( "Regla 1 Y 2 Juntas Como Una Sola Formula")

print ("Creando Formula Para Iniciar DPLL")
print ("Formula Demasiado Larga Puede Tardar Unos Segundos")
# Creo la formula como objeto

#print ("Formula: ", T.Inorder(A1))(OJO NO SE PUEDE IMPRIMIR FORMULA DEMASIADO GRANDE,ERROR DE MEMORIA PARA RECURSION)
print ("Iniciaremos DPPL ")


A = FORM.StringtoTree('0203-04-05-06-0911-13-16-01-07-0812-14-1510-YYYYYYYYYYYYYYY', letrasProposicionales) #Prueba muy corta para comprobar

#A = FORM.StringtoTree(conjunciones, letrasProposicionales)

A = FORM.quitarDobleNegacion(A)

A = FORM.reemplazarImplicacion(A)

A = FORM.quitarDobleNegacion(A)

A = FORM.deMorgan(A)

A = FORM.quitarDobleNegacion(A)

OK = True
while OK:
	OK, A = FORM.aplicaDistributiva(A)

conjuntoClausulas = FORM.pasaraclaus(A)

print("Conjunto de disyunciones de literales:\n ", conjuntoClausulas)

Inter ={}

def interpetr(l):
    # Devuelve el complemento de un literal
    # Input: l, que es una cadena con un literal (ej: p, -p)
    # Output: l complemento
	if '-' in l:
		return False
	else:
		return True

def complemento(l):
    # Devuelve el complemento de un literal
    # Input: l, que es una cadena con un literal (ej: p, -p)
    # Output: l complemento
	if '-' in l:
		return l[1:]
	else:
		return '-' + l

def unit_propagate(Set,Int):
    #print("set",Set)
    #print("int",Int)

    if len(Set)==0:
        return [],Int

    indice = 0
    for clausula in Set:
            print(clausula)
            if(len(clausula) == 0):	# En este caso tiene una clausula vacia
                return False,{}	

            elif(len(clausula)==1):
                comp = complemento(clausula[0]) # aca saca el complemento
                Int_literal = interpetr(clausula[0])
                clausula1=clausula[0]
                if '-' not in clausula1:
                    Int[clausula1]= Int_literal
                else:
                    Int[comp]=Int_literal
                Set.pop(indice)
                lista_indice=[]

                for clausula2 in Set:# Aca elemina el complemento  
                    indice2 = 0
                    for i in clausula2:
                        if i == comp:
                            clausula2.pop(indice2)
                        if i == clausula1:
                            lista_indice.append(indice2)
                            indice2 = indice2 +1
                for i in lista_indice:
                    Set.pop(i)

                return unit_propagate(Set,Int)   # Aca viene la recursion

            elif(len(clausula)!=1):
                indice = indice +1
                if (indice == len(Set)):
                    return Set,Int


def Despues_propagate(Set,Int):
    Conjunto , Interpretacion = unit_propagate(Set,Int)
    if len(Conjunto)==0 :
        return True,Interpretacion
    for i in Conjunto:
        if len(i)==0:
            return False,{}
    else:
        return Set,Int

def DPLL_1(Set,Int):
    inicial =''
    for clausula in Set:
        for i in clausula:
            seleccion = 0
            indice = 0
            if i not in Int and len(Set)!=0:
                seleccion = seleccion +1
                comp = complemento(i) # aca saca el complemento
                Int_literal = interpetr(i)
                clausula1=i
                if seleccion == 0:
                    inicial = comp
                if '-' not in clausula1:
                    Int[clausula1]= Int_literal
                else:
                    Int[comp]=Int_literal
                Set.pop(indice)
                indice +=1
                lista_indice=[]

                for clausula2 in Set:# Aca elemina el complemento  
                    indice2 = 0
                    for i in clausula2:
                        if i == comp:
                            clausula2.pop(indice2)
                        if i == clausula1:
                            lista_indice.append(indice2)
                            indice2 = indice2 +1
                for i in lista_indice:
                    Set.pop(i)
    if len(Set)==0:
        return True,Int,seleccion
    else:
        return Set,Int,seleccion

def DPLL_compl(Set,Int,i):
                Set1 = Set.copy()
                comp = complemento(i) # aca saca el complemento
                Int_literal = interpetr(i)
                clausula1=i
                if '-' not in clausula1:
                    Int[clausula1]= Int_literal
                else:
                    Int[comp]=Int_literal
                Set1.pop(indice)
                indice +=1
                lista_indice=[]

                for clausula2 in Set1:# Aca elemina el complemento  
                    indice2 = 0
                    for i in clausula2:
                        if i == comp:
                            clausula2.pop(indice2)
                        if i == clausula1:
                            lista_indice.append(indice2)
                            indice2 = indice2 +1
                for i in lista_indice:
                    Set1.pop(i)
                return Set1,Int


def DPLL(Set,Int):
    Set1 = Set.copy()
    Int1 = Int.copy()
    Conjunto,Interpretacion=Despues_propagate(Set1,Int1)
    if Conjunto == True:
            return True,Interpretacion
    else:
            Conjunto,Interpretacion,comp = DPLL_1(Conjunto,Interpretacion)
            if Conjunto == True :
                    return True,Interpretacion
            else:
                    Conjunto,Interpretacion = DPLL_compl(Set1,{},comp)
                    if Conjunto == True:
                            return True,Interpretacion
                    else:
                         Conjunto,Interpretacion,comp = DPLL_1(Conjunto,Interpretacion)
                         if Conjunto == True:
                                 return True,Interpretacion
                         else:
                                 return False,Interpretacion


# TRUE : Satisfacible
# FALSE : Insatisfacible



Inter={}
lista=[]
Conjunto, INTS = DPLL(conjuntoClausulas,Inter)
print("True : Satisfacible , False : Insatisfacible")

print("-------",INTS)
for i in INTS:
        if INTS[i]:
                lista.append(i)
        else:
                lista.append("-"+i)
if Conjunto == (True):
    if len(lista) == 0:
        print (u"Error: la lista de interpretaciones está vacía")
    else:
        print ("Guardando interpretaciones en archivo...")
        import csv
        archivo = ('tableros_automatico.csv')
        with open(archivo, 'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows([lista])

        print ("Interpretaciones guardadas  en " + archivo)

        import Tablero as V
        print ("Dibujando su tablero: ")
        V.dibujar([lista])

print ("FIN")

