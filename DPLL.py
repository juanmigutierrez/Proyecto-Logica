

# Algoritmo DPLL


disyuncion = [['-q'],['-q', '-r'], ['-q', '-p'],['r','t']]
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
                    print("clausula2",clausula2)
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
    for clausula in Set:
        for i in clausula:
            indice = 0
            if i not in Int and len(Set)!=0:
                comp = complemento(i) # aca saca el complemento
                Int_literal = interpetr(i)
                clausula1=i
                if '-' not in clausula1:
                    Int[clausula1]= Int_literal
                else:
                    Int[comp]=Int_literal
                Set.pop(indice)
                indice +=1
                lista_indice=[]

                for clausula2 in Set:# Aca elemina el complemento  
                    print("clausula2",clausula2)
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
        return True,Int
    else:
        return Set,Int

def DPLL(Set,Int):
    Conjunto,Interpretacion=Despues_propagate(Set,Int)
    return DPLL_1(Set,Int)

DPLL(disyuncion,Inter)



