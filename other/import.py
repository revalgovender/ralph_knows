import json

file = open('../data/units.json')
data = json.load(file)

file = open('app.json')
luke_data = json.load(file)

unit_counter_list = {}
counter = 1

for data in data.items():
    unit_data = data[1]
    unit_image = ''

    for luke in luke_data:
        luke_units = luke['units']
        for luke_unit in luke_units:
            if unit_data['actual-name'] == luke_unit['name']:
                unit_image = luke_unit['icon_url']

    unit_counter_list.update({
        counter: {
            "aliases": unit_data['aliases'],
            "actual-name": unit_data['actual-name'],
            "general": unit_data['general'],
            "strength": unit_data['strength'],
            "weakness": unit_data['weakness'],
            "icon": unit_image,
        }
    })
    counter = counter + 1

json_object = json.dumps(unit_counter_list, indent=4)

with open("units-1.json", "w") as outfile:
    outfile.write(json_object)