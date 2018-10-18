print "Funcion que pasa de una formula como cadena a un objeto Tree\n\
Recuerde que la formula debe estar escrita en notacion polaca invertida\n \
Las unicas letras proposicionales permitidas son p, q, r, s, t, v\n \
Claves de escritura para los conectivos:\n \
La negacion se escribe -\n \
La Or se escribe O\n \
El AND se escribe Y\n \
La implicacion se escribe >"
letrasProposicionales = ['1', '2', '3', '4', '5', '6','7','8','9','11','12','13','14','15','16','10']
conectivos = ['O', 'Y', '>','-']
# Definimos la clase de objetos Tree para las formulas
class Tree(object):
    def __init__(self,l,iz,der):
        self.left = iz
        self.right = der
        self.label = l

# Define la funcion de imprimir rotulos Inorder(f)
def Inorder(f):
    # Determina si F es una hoja
    if f.right == None:
#        print "Es una hoja!"
        print f.label,
    elif f.label == '-':
        print f.label,
        Inorder(f.right)
    else:
        print "(",
        Inorder(f.left)
        print f.label,
        Inorder(f.right)
        print ")",

# Solicitamos una cadena
f = raw_input('Ingrese una cadena: ') or 'rqpO>' # Cadena por defecto
cadena=[]
print "Cadena ingresada " + f
word=""
cont=0
for j in f:
    if j!=" " and j not in conectivos:
        word=word+j
    if j==" " or cont==len(f)-1:
        cadena.append(word)
        word=""
    if j in conectivos:
        cadena.append(word)
        cadena.append(j)
        word=""
    cont=cont+1
print cadena



pila = [] # inicializamos la pila

for c in cadena:
    if c in letrasProposicionales:
        pila.append(Tree(c, None, None))
    elif c == '-':
        aux = Tree(c, None, pila[-1])
        del pila[-1]
        pila.append(aux)
    elif c in conectivos:
        aux = Tree(c, pila[-1], pila[-2])
        del pila[-1]
        del pila[-1]
        pila.append(aux)

formula = pila[-1]

print "La formula ",
Inorder(formula)
print " fue creada como un objeto!"
