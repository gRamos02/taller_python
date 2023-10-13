#  Programa que dada dos listas, regresa una con los numeros en comun
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = set()

for i in a:
    if i in b:
        c.add(i)

print(c)

#One liner
print(set(a[x] for x in range(len(a))if a[x] in b));