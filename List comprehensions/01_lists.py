numbers = []

for element in range(1,11):
    numbers.append(element)
print(numbers)

#element for element in iterable
numbers_v2 = [element for element in range(1,11)]
print(numbers_v2)

numbers_v3 = []
for element in range(1,11):
    numbers_v3.append(element*2)
print(numbers_v3)

numbers_v4 = [element*2 for element in range(1,11)]
print(numbers_v4)

#con condiciones
numbers_v5 = [i*2 for i in range(1,101) if i%2==0]
print(numbers_v5)
print(len(numbers_v5))