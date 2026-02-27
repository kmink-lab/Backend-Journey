#1 Mostrar los números del 1 al 10
for i in range(1, 11):
    print (i)

#2 Mostrar solo los números pares del 1 al 20
#for i in range(1, 21):
#    if i % 2 == 0:
#    return (i)

#3 Contar cuántos números son mayores a 10 en una lista
#numeros = [3, 15, 7, 22, 9, 30]
#res = 0
#for i, num in enumerate(numeros):
#    if num > 10:
#        res = res + 1
#    elif num < 10:
#        res = res
#print(res)

#version simplificada
#res = 0
#for num in numeros:
#    if num > 10:
#        res += 1
#print(res)

#4 Creá una función que:
#reciba una edad
#devuelva "mayor" o "menor"
#No imprimas dentro de la función.
#Devolvé el resultado.

#def mayor_menor(edad):
#    if int(edad) > 18:
#        return("Mayor.")
#    else:
#        return("Menor.")
#edad = input("Por favor ingrese su edad: ")
#mayor_menor(edad)

#5 Función que:
#reciba una lista de números
#devuelva el promedio
#Pistas:
#suma
#cantidad
#división

#lista = [2, 5, 67, 101, 12, 34]
#def promediador(lista):
#    total = 0
#    it = 0
#    for i, num in enumerate(lista):
#        total = total + num
#        it = it + 1
#    return(f"El promedio de la lista es: {int(total/it)}")
#promediador(lista)