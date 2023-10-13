import read_csv
import charts
import utils


if __name__ == '__main__':
    data = read_csv.get_csv_data('Gráficas\Proyecto\world_population.csv')
    world_percentage  = utils.get_world_percentage(data)

    names = list(world_percentage.keys())
    percentages = list(world_percentage.values())
    
    charts.create_pie_chart(names,percentages)