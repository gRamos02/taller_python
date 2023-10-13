import csv

def get_csv_data(path):
    data = []
    with open(path) as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            it = zip(header,row)
            cdict = {key:value for key,value in it}
            data.append(cdict)
    return data



if __name__ == '__main__':
    get_csv_data('Gráficas\Proyecto\world_population.csv')