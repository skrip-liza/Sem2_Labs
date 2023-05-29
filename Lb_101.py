import json

with open('spisok.json') as json_file:

    data = json.load(json_file)
    data_split = list(data['products'])
    for i in range(len(data_split)):
        print('Название: ' + data_split[i]['name'])
        print('Цена: ' + str(data_split[i]['price']))
        print('Вес: ' + str(data_split[i]['weight']))
        if (data_split[i]['available']):
            print("В наличии")
        else:
            print("Нет в наличии")
        print('')
