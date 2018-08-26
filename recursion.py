letrasProposicionales=['p','q','r','s','t']
conectivosBinarios=['Y','O','>','<>']
negacion=['-']

class Tree(object):
    def __init__(self,l,iz,der):
        self.left=iz
        self.right=der
        self.label=l

def Num_Hojas(arb):
    if arb.right == None:
        return 1
    else:
        return Num_Hojas(arb.left)+Num_Hojas(arb.right)
    
def whatis(arb):
    if arb.label in letrasProposicionales:
        return "La formula es una letra proposicional '%s'"%(arb.label)
    elif arb.label in negacion:
        return "Rama con conectivo de negacion '%s'" %(arb.label)
    else:
        return "Rama con conectivo binario '%s'" %(arb.label)
def Num_Conect(arb):
    if arb.label in letrasProposicionales:
        return 0
    elif arb.label in negacion:
        return 1+Num_Conect(arb.right)
    elif arb.label in conectivosBinarios:
        return 1+Num_conect(arb.right)+Num_conect(arb.left)
    else:
        return "Rotulo incorrecto"
def inorder(arb):
    if arb.label in letrasProposicionales:
        return arb.label
    elif arb.label in negacion:
        return arb.label+inorder(arb.right)
    elif arb.label in conectivosBinarios:
        return '('+inorder(arb.left)+' '+arb.label+' '+inorder(arb.right)+' '+')'
    else:
        return "Rotulo incorrecto"

    #Este metodo retorna una lista de diccionarios con todos los valores de verdad posibles para cada letra
def interpretaciones():
    aux= {}
    interps= []
    for a in letrasProposicionales:
        aux[a] = 'V'
    interps.append(aux)
    for a in letrasProposicionales:
        interps_aux = [i for i in interps]

        for i in interps_aux:
            aux1={}
            for b in letrasProposicionales:
                if a==b:
                    aux1[b]='F'
                else:
                    aux1[b]=i[b]
            interps.append(aux1)
    return interps
def valor(arb,interpretaciones):
    if arb.right== None:
        return interpretaciones[arb.label]
    elif arb.label == '-':
        if valor(arb.right,interpretaciones)=='V':
            return 'F'
        else:
            return 'V'
    elif arb.label == 'Y':
        if valor(arb.left,interpretaciones)== 'V' and valor(arb.right,interpretaciones)=='V':
            return 'V'
        else:
            return 'F'
    elif arb.label == 'O':
        if valor(arb.left,interpretaciones)=='V' or valor(arb.right,interpretaciones)=='V':
            return 'V'
        else:
            return 'F'
    elif arb.label == '>':
        if valor(arb.left,interpretaciones)=='F' or valor(arb.right,interpretaciones)=='V':
            return 'V'
        else:
            return 'F'
    elif arb.label =='<>':
        if valor(arb.left,interpretaciones) == valor(arb.right,interpretaciones):
            return 'V'
        else:
            return 'F'      
    #Este metodo imprime si dos formulas son equivalentes o no lo son
def equivalencia(arb1,arb2):
    for i in interpretaciones():
        if valor(arb1,i)!=valor(arb2,i):
            return "%s  VS  %s  No son Equivalentes" %(inorder(arb1),inorder(arb2))
    return "%s  VS  %s  Son Equivalentes" %(inorder(arb1),inorder(arb2))
#Este metodo imprime todas las posibles opciones para que una formula sea verdadera
def valoresverdaderos(arb1):
    print "%s es verdadero para:\n" %(inorder(arb1))
    for i in interpretaciones():

        if valor(arb1,i)== 'V':
            print i
            
#imprime las posibles interpretaciones
print "Interpretaciones posibles:"
for i in interpretaciones():
    print i

A1=Tree('p',None,None)
A2 = Tree('-',None,A1)
A3 = Tree('-',None,A2)

print '----------------'
print ' ejemplo si funciona problema'
print equivalencia(A1,A2)
print equivalencia(A1,A3)

#punto 4
#a)
#Arbol1 
A1 = Tree('r',None,None)
A2 = Tree('q',None,None)
A3 = Tree('p',None,None)
A4 = Tree('O',A2,A1)
A5 = Tree('Y',A3,A4)
#Arbol2
B1 = Tree('r',None,None)
B2 = Tree('q',None,None)
B3 = Tree('p',None,None)
B4 = Tree('Y',B3,B1)
B5 = Tree('Y',B3,B2)
B6 = Tree('O',B4,B5)
print'------'
print 'punto a'

print equivalencia(A5,B6)
#a)
#Arbol1
A1 = Tree('p',None,None)
A2 = Tree('q',None,None)
A3 = Tree('O',A1,A2)
#Arbol2
A4 = Tree('-',None,A1)
A5 = Tree('-',None,A2)
A6 = Tree('Y',A5,A4)
A7 = Tree('-',A5,A6)


print'------'
print 'punto b'

print equivalencia(A3,A7)

#c)
#Arbol1
A1 = Tree('p',None,None)
A2 = Tree('q',None,None)
A3 = Tree('Y',A1,A2)
#Arbol2
A4 = Tree('-',None,A1)
A5 = Tree('-',None,A2)
A6 = Tree('O',A5,A4)
A7 = Tree('-',None,A6)
print'------'
print 'punto c'
print equivalencia(A3,A7)

print'------'
print 'punto d'
#arbol1
A1 = Tree('p',None,None)
A2 = Tree('q',None,None)
A3 = Tree('>',A1,A2)

#arbol 2
A4 = Tree('-',None,A1)
A6 = Tree('O',A4,A2)

print equivalencia(A3,A6)
print '-------------------'
print"Punto 2: \n"
#siguiente punto del taller
#arbol:
A1 = Tree('p',None,None)
A2 = Tree('q',None,None)
A3 = Tree('r',None,None)
A4 = Tree('s',None,None)
A5 = Tree('t',None,None)
A6 = Tree('O',A3,A4)#r O s
A7 = Tree('>',A1,A2)#p > q
A8 = Tree('-',None,A7)#-(p>q)
A9 = Tree('>',A8,A6)#-(p>q) > r O s
A10=Tree('Y',A9,A5)# (-(p>q) > r O s) Y t
valoresverdaderos(A10)

