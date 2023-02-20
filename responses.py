import json


def get_response(message: str) -> str:
    user_supplied_unit_name = message.lower()

    print('1')

    if user_supplied_unit_name == 'hello':
        return 'Hey there!'

    if user_supplied_unit_name == '!help':
        return '`This is a help message that you can modify.`'

    file = open('data/units.json')
    data = json.load(file)

    for unit in data.items():
        if user_supplied_unit_name in unit[1]['aliases']:
            return unit[1]['unit-data']

    return 'I didn\'t understand what you wrote. Try typing "!help".'
