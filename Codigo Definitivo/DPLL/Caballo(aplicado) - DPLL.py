#-*-coding: utf-8-*-
print ("Importando paquetes...")
from timeit import default_timer as timer
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
################################################## CODIGO EDGAR ##############################################

class Tree(object):
	def __init__(self, r, iz, der):
		self.left = iz
		self.right = der
		self.label = r

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula

    if f.right == None:
        return f.label
    elif f.label == '-':
        return f.label + Inorder(f.right)
    else:
        return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def StringtoTree(A, letrasProposicionales):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree
    conectivos = ['O', 'Y', '>','-']
    cadena=[]
    cont=0
    while cont < len(A):
        if A[cont] in conectivos:
                cadena.append(A[cont])
                cont+=1
        else:
            cadena.append(A[cont]+A[cont+1])
            cont+=2
	    #print cont
            #print cadena
    conectivos = ['O', 'Y', '>']    
        #print cadena
    pila = []
    for c in cadena:
        if c in letrasProposicionales:
            pila.append(Tree(c, None, None))
        elif c == '-':
            formulaAux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(formulaAux)
        elif c in conectivos:
            #print cadena
            #print c
            formulaAux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(formulaAux)
    print ("La formula fue creada como un objeto!")
    return pila[-1]

def quitarDobleNegacion(f):
	# Elimina las dobles negaciones en una formula como arbol
	# Input: tree, que es una formula de logica proposicional
	# Output: tree sin dobles negaciones

	if f.right == None:
		return f
	elif f.label == '-':
		if f.right.label == '-':
			return quitarDobleNegacion(f.right.right)
		else:
			return Tree('-', \
						None, \
						quitarDobleNegacion(f.right)\
						)
	else:
		return Tree(f.label, \
					quitarDobleNegacion(f.left), \
					quitarDobleNegacion(f.right)\
					)

def reemplazarImplicacion(f):
    # Regresa la formula reemplazando p>q por -pOq
    # Input: tree, que es una formula de logica proposicional
    # Output: tree

    if f.right == None:
        return f
    elif f.label == '-':
        return Tree('-', None, reemplazarImplicacion(f.right))
    elif f.label == '>':
        noP = Tree('-', None, reemplazarImplicacion(f.left))
        Q = reemplazarImplicacion(f.right)
        return Tree('O', noP, Q)
    else:
        return Tree(f.label, reemplazarImplicacion(f.left), reemplazarImplicacion(f.right))

def deMorgan(f):
    # Regresa la formula aplicando deMorgan -(pYq) por -pO-q
    # Input: tree, que es una formula de logica proposicional
    # Output: tree

	if f.right == None:
		return f
	elif f.label == '-':
		if f.right.label == 'Y':
			print(u"La fÃ³rmula coincide negaciÃ³n Y")
			return Tree('O', \
						Tree('-', None, deMorgan(f.right.left)),\
						Tree('-', None, deMorgan(f.right.right))\
						)
		elif f.right.label == 'O':
			print(u"La fÃ³rmula coincide negaciÃ³n O")
			return Tree('Y', \
						Tree('-', None, deMorgan(f.right.left)),\
						Tree('-', None, deMorgan(f.right.right))\
						)
		else:
			return Tree('-', \
						None, \
						deMorgan(f.right) \
						)
	else:
		return Tree(f.label, \
					deMorgan(f.left),\
					deMorgan(f.right)\
					)

def distributiva(f):
    # Distribuye O sobre Ys: convierte rO(pYq) en (rOp)Y(rOq)
    # Input: tree, que es una formula de logica proposicional
    # Output: tree

	if f.right == None:
		# print("Llegamos a una rama")
		return f
	elif f.label == 'O':
		# print("Encontramos O...")
		if f.left.label == 'Y':
			# print("... encontramos Y a la izquierda")
			P = f.left.left
			Q = f.left.right
			R = f.right
			return Tree('Y', \
						Tree('O', P, R), \
						Tree('O', Q, R)
						)
		if f.right.label == 'Y':
			# print("... encontramos Y a la derecha")
			R = f.left
			P = f.right.left
			Q = f.right.right
			return Tree('Y', \
						Tree('O', R, P), \
						Tree('O', R, Q)
						)
		else:
			# print("... pero no hay Y")
			# print("Pasamos a hijos de O")
			return Tree(f.label, \
						distributiva(f.left), \
						distributiva(f.right)
						)
	elif f.label == '-':
		# print("Pasamos a hijo de negacion")
		return Tree('-', \
					None, \
					distributiva(f.right)
					)
	else:
		# print("Pasamos a hijos de ", f.label)
		return Tree(f.label, \
					distributiva(f.left), \
					distributiva(f.right)
					)

def aplicaDistributiva(f):
    # Devuelve True si la distributiva de f es distinta a f
    # Input: tree, que es una formula de logica proposicional
    # Output: - True/False,
	# 		  - tree
	aux1 = Inorder(f)
	print("Se analiza: ", aux1)
	B = distributiva(f)
	aux2 = Inorder(B)
	print("Se obtuvo : ", aux2)
	if  aux1 != aux2:
		print(u"Hubo distribuciÃ³n")
		return True, B
	else:
		print(u"No hubo distribuciÃ³n")
		return False, f

def eliminaConjunciones(f):
    # Devuelve una lista de disyunciones de literales
    # Input: tree, que es una formula en CNF
    # Output: lista de cadenas
	if f.label == None:
		print("Oh, Oh, problemas, es una letra proposicional!")
	elif f.label == 'O':
		return [Inorder(f)]
	elif f.label == 'Y':
		return eliminaConjunciones(f.left) + eliminaConjunciones(f.right)
	else:
		print("Oh, Oh, la formula no estaba en CNF!")

def complemento(l):
    # Devuelve el complemento de un literal
    # Input: l, que es una cadena con un literal (ej: p, -p)
    # Output: l complemento
	if '-' in l:
		return l[1:]
	else:
		return '-' + l

def formaClausal(f):
    # Obtiene la forma clausal de una formula en CNF
    # Input: tree, que es una formula de logica proposicional
    # Output: lista de clausulas

	# Primero elimino las conjunciones, obteniendo
	# una lista de disyunciones de literales
	print("Encontrando lista de disyunciones de literales...")
	aux = eliminaConjunciones(f)
	badChars = ['(', ')']
	conjuntoClausulas = []
	for C in aux:
		C = ''.join([x for x in C if x not in badChars])
		C = C.split('O')
		conjuntoClausulas.append(C)

	aux = []
	print(u"Eliminando clÃ¡usulas triviales...")
	for C in conjuntoClausulas:
		trivial = False
		for x in C:
			xComplemento = complemento(x)
			if xComplemento in C:
				print(u"ClÃ¡usula trivial encontrada")
				trivial = True
				break
		if not trivial:
			aux.append(C)

	print("Eliminando repeticiones...")
	# Eliminamos repeticiones dentro de cada clausula
	aux = [list(set(i)) for i in aux]
	# Eliminamos clausulas repetidas
	aux_set = set(tuple(x) for x in aux)
	aux = [list(x) for x in aux_set]

	conjuntoClausulas = aux

	return conjuntoClausulas

############################## CODIGO EDGAR #####################


A = StringtoTree(conjunciones, letrasProposicionales)

A = quitarDobleNegacion(A)

A = reemplazarImplicacion(A)

A = quitarDobleNegacion(A)

A = deMorgan(A)

A = quitarDobleNegacion(A)

OK = True
while OK:
	OK, A = aplicaDistributiva(A)

conjuntoClausulas = formaClausal(A)

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
    print("set",Set)
    print("int",Int)

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
    if Conjunto == True :
        return True,Interpretacion
    else:
        Conjunto,Interpretacion,comp = DPLL_1(Conjunto,Interpretacion)
        if Conjunto == True :
            return True,Interpretacion
        else:
            Conjunto,Interpretacion = DPLL_compl(Set1,{},comp)
            Conjunto,Interpretacion,comp = DPLL_1(Conjunto,Interpretacion)
            if Conjunto == True:
                return True,Interpretacion
            else:
                return False,Interpretacion


# TRUE : Satisfacible
# FALSE : Insatisfacible



Inter={}

Conjunto, Interpretacion = DPLL(conjuntoClausulas,Inter)
print("True : Satisfacible , False : Insatisfacible")

if Conjunto == (True):
    if len(INTS) == 0:
        print (u"Error: la lista de interpretaciones estÃ¡ vacÃ­a")
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

