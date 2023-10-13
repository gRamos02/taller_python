# Dada una lista, imprimir todos los numeros que sean menor a cinco
"""
1. En lugar de imprimir los elementos uno a uno, haz una nueva lista que tenga todos los elementos menores que 5 de esta lista e imprime esta nueva lista.
2. Escribe esto en una línea de Python.
3.Pide al usuario un número y devuelve una lista que contenga sólo los elementos de la lista original a que sean menores que el número dado por el usuario.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# basic problem:
for x in a:
    if x< 5: print(x)

# combine challenges 1 and 2:
print( [ x for x in a if x<5 ] )