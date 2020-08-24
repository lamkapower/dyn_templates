from django.shortcuts import render
from django.conf import settings
import csv


def set_color(list_of_numbers):
    def _take_color(data, position):
        new_data = {"color": "white", "data": "-"}
        if position == 0:
            new_data['data'] = data
            return new_data

        if data != '':
            number = float(data)
            if number > 5:
                new_data['color'] = 'red darken-4'
            elif number > 2:
                new_data['color'] = 'red'
            elif number > 1:
                new_data['color'] = 'red lighten-4'
            elif number < 0:
                new_data['color'] = 'teal darken-2'
            new_data['data'] = number

        if position == 13:
            new_data['color'] = 'grey'

        return new_data

    output_list = list()
    for i, n in enumerate(list_of_numbers):
        output_list.append(_take_color(n, i))

    return output_list


def inflation_view(request):
    with open(settings.INFLATION_CSV, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        other_data = []
        for number, data in enumerate(reader):
            if number == 0:
                months = data[0].split(';')
            else:
                other_data.append(set_color(data[0].split(';')))
        return render(request, 'app\inflation.html', context={'months': months, 'other_data': other_data})
