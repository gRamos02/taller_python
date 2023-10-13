import functools

numbers = [1,2,3,4]
result = functools.reduce(lambda counter,item: counter+item, numbers)
print(result)

def accum(counter,item):
    print('counter = ',counter)
    print('item = ',item)
    return counter+item

result_2 = functools.reduce(accum, numbers)
print(result_2)