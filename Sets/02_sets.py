#Operaciones con sets

set_countries = {'mex', 'col', 'arg'}
size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

#add
set_countries.add('pe')
print(set_countries)

#update
set_countries.update({'bol','chil','mex'})
print(set_countries)

#remove
set_countries.remove('arg')
print(set_countries)

#clear
set_countries.clear()
print(set_countries)