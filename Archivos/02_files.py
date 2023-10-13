with open('Archivos/text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('\ntexto nuevo')

