import json


def get_everything_after(string, sub):
    index = string.find(sub)
    if index != -1:
        index = index + len(sub)
        return string[index:]
    else:
        raise Exception('Sub string not found!')


def get_everything_before(string, sub):
    index = string.find(sub)
    if index != -1:
        return string[:index]
    else:
        print(string)
        raise Exception('Sub string not found!')


file = open('source-data/unit-counters.json')
data = json.load(file)

unit_counter_list = {}
counter = 1

for data in data.items():
    unit_name = get_everything_before(data[1], '</b>')
    unit_name = get_everything_after(unit_name, '<b>')
    unit_name_lower = unit_name.lower()
    unit_name_plural = unit_name.lower() + 's'
    unit_data = get_everything_after(data[1], 'prefixreval')
    unit_data = get_everything_before(unit_data, '</i><br>')
    unit_data = get_everything_before(unit_data, '<i>')
    unit_counter_list.update({
        counter: {
            "aliases": [
                unit_name_lower,
                unit_name,
                unit_name_plural
            ],
            "actual-name": unit_name,
            "unit-data": unit_data
        }
    })
    counter = counter + 1

json_object = json.dumps(unit_counter_list, indent=4)

with open("data-cleaner-output/output/units.json", "w") as outfile:
    outfile.write(json_object)
