import read_csv
def get_world_percentage(data):
    cdict = {}
    for country in data:
        cdict[country['Country/Territory']] = float(country['World Population Percentage'])
    return cdict

if __name__ == '__main__':
    get_world_percentage(read_csv.get_csv_data('Gráficas\Proyecto\world_population.csv'))