#Map ejecuta una funcion por cada iterable

numbers = [1,2,3,4]

numbers_v2 = map(lambda i:i*2, numbers)
numbers_v2 = list(numbers_v2)
print(numbers_v2)