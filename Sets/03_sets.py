#Operaciones con conjuntos
set_a = {'col','mex', 'bol'}
set_b = {'pe','bol'}

#union
set_c = set_a.union(set_b)
print(set_c)

#interseccion
set_d = set_a.intersection(set_b)
print(set_d)

#diferencias
set_e = set_a.difference(set_b)
print(set_e)

#diferencia simetrica
set_f = set_a.symmetric_difference(set_b)
print(set_f)