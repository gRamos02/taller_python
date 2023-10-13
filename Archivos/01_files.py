file = open('Archivos/text.txt')
#print(file.read())
#print(file.readline())

#for line in file:
#    print(line)

file.close()

with open('Archivos/text.txt') as file:
    for line in file:
        print(line)