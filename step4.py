#Hackerrank exercise 6/30

#a = input().split()

#b = int(a[0])

#a = a[1:]

#print(a,b, sep="\n")

#def indexSep(word):

#    e = ""
#    o = ""

#    for i in range(len(word)):
        
#        if i == 0 or i%2 == 0:
#            e = e + word[i]
#        elif i != 0 and i%2 != 0:
#            o = o + word[i]

    #print(e, o)
#    return e, o

#indexSep(a[1])

#ret = map(indexSep, a)

#for e, o in map(indexSep, a):
#    print(e, o)

### EASIER

n = int(input())
#Guardo el entero que declara la cantidad de inputs que se van a ingresar

def indexSep(word):
    return word[::2], word[1::2]
#Pide una palabra y devuelve esa palabra primero por un lado con los indices pares [::2]
# y por otro con los indices impares [1::2]

for _ in range(n):
    # uso _ porque no necesito utilizarlo como variable
    e, o = indexSep(input())
    # Por cada n vuelta definida con el entero ingresado, se solicita el nuevo input y
    # se aplica la funcion de arriba
    print(e, o)