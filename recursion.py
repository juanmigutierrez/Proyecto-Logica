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
def equivalencia(arb1,arb2):
    for i in interpretaciones():
        if valor(arb1,i)!=valor(arb2,i):
            return "%s  VS  %s  No son Equivalentes" %(inorder(arb1),inorder(arb2))
    return "%s  VS  %s  Son Equivalentes" %(inorder(arb1),inorder(arb2))


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


