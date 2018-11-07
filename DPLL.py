

# Algoritmo DPLL


disyuncion = [['-q'],['-q', '-r'], ['-q', '-p']]
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
    Set1 = Set
    print(Set1)
    print(Int)

    if len(Set)==0:
        return True,Int

    indice = 0
    for clausula in Set1:
            print(clausula)
            if(len(clausula) == 0):	# En este caso tiene una clausula vacia
                return False,{}	

            elif(len(clausula)==1):
                comp = complemento(clausula[0]) # aca saca el complemento
                Int_literal = interpetr(clausula[0])
                Int[clausula[0]]= Int_literal
                Set1.pop(indice)

                for clausula2 in Set: # Aca elemina el complemento
                    indice2 = 0
                    for i in clausula2:
                        if i == comp:
                            clausula2.pop(indice2)
                        indice2 = indice2 +1

 
                unit_propagate(Set1,Int)   # Aca viene la recursion

            elif(indice==len(Set)-2):
                return Set,Int
            else:
                indice = indice +1



Conjunto , Interpretacion = unit_propagate(disyuncion,Inter)
print(Conjunto,Interpretacion)


def Despues_propagate(Set,Int):

