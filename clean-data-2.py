import json


def get_everything_after(string, sub):
    index = string.find(sub)
    if index != -1:
        index = index + len(sub)
        return string[index:]
    else:
        print(string)
        raise Exception('Sub string not found!')


def get_everything_after_including(string, sub):
    index = string.find(sub)
    if index != -1:
        index = index
        return string[index:]
    else:
        print(string)
        raise Exception('Sub string not found!')


def get_everything_before(string, sub):
    index = string.find(sub)
    if index != -1:
        return string[:index]
    else:
        print(string)
        raise Exception('Sub string not found!')


file = open('data/units.json')
data = json.load(file)

unit_counter_list = {}
counter = 1

for data in data.items():
    unit_data = data[1]

    strength = get_everything_before(unit_data['unit-data'], 'Weak')
    strength = get_everything_after(strength, 'Strong vs. ')
    weakness = get_everything_after(unit_data['unit-data'], 'Weak vs. ')
    general = get_everything_before(unit_data['unit-data'], 'Strong')
    unit_counter_list.update({
        counter: {
            "aliases": unit_data['aliases'],
            "actual-name": unit_data['actual-name'],
            "general": general,
            "strength": strength,
            "weakness": weakness,
        }
    })
    counter = counter + 1

json_object = json.dumps(unit_counter_list, indent=4)

with open("data-cleaner-output/units-1.json", "w") as outfile:
    outfile.write(json_object)
