#-*-coding: utf-8-*-
print ("Importando paquetes...")
from timeit import default_timer as timer
import FormaClausal as FORM
print ("Importados!")

# Guardo el tiempo al comenzar el procedimiento
start = timer()

# Regla 1: Debe haber exactamente tres caballos

# Creo las letras proposicionales
letrasProposicionales = []
s=""
for i in range(1, 10):
        if i < 10:
                s+="0"
        letrasProposicionales.append(s+str(i))
        s=""

# print "Letras proposicionales: ", letrasProposicionales

# Regla 1: Debe haber exactamente tres caballos
conjunciones = '' # Para ir guardando las conjunciones de trios de disyunciones de literales
inicial = True # Para inicializar la primera conjuncion

for p in letrasProposicionales:
    aux1 = [x for x in letrasProposicionales if x != p] # Todas las letras excepto
    # print "aux1: ", aux1
    for q in aux1:
        aux2 = [x for x in aux1 if x != q] # Todas las letras excepto p y q
        # print "aux2", aux2
        for r in aux2:
            literal = r + q + p + 'Y' + 'Y'
            aux3 = [x + '-' for x in aux2 if x != r]
            for k in aux3:
                literal = k + literal + 'Y'
            # print "Literal: ", literal
            if inicial: # Inicializar la primera conjuncion
                conjunciones = literal
                inicial = False
            else:
                conjunciones = literal + conjunciones + 'O'

        # print "Conjunciones: ", conjunciones

# Regla 2: Ningun caballo debe poder atacar a otro

conjunciones = '08-06-Y01>' + conjunciones + 'Y'
conjunciones = '09-07-Y02>' + conjunciones + 'Y'
conjunciones = '08-04-Y03>' + conjunciones + 'Y'
conjunciones = '09-03-Y04>' + conjunciones + 'Y'
conjunciones = '07-01-Y06>' + conjunciones + 'Y'
conjunciones = '06-02-Y07>' + conjunciones + 'Y'
conjunciones = '03-01-Y08>' + conjunciones + 'Y'
conjunciones = '04-02-Y09>' + conjunciones + 'Y'

A = FORM.StringtoTree(conjunciones, letrasProposicionales)

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

