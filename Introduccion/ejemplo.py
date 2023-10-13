
lista = [1,2,3,4,5,6]
diccionario = {
    'color': 'azul',
    'size': 'XL'
}

it = iter(lista)
it_d = iter(diccionario.values())
print(type(it))
print(type(it_d))

for i in it_d:
    print(i)

while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break

def saludo(name: str) -> str:
    return 'Hola ' + name

print(saludo(12))