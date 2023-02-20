import json


def get_response(message: str) -> str:
    user_supplied_unit_name = message.lower()

    if user_supplied_unit_name == 'hello':
        return 'Hey there!'

    if user_supplied_unit_name == '!help':
        return '`This is a help message that you can modify.`'

    file = open('data/units.json')
    data = json.load(file)

    for unit in data.items():
        if user_supplied_unit_name in unit[1]['aliases']:
            return '\n\n💬 General:\n' + unit[1]['general'] + '\n\n😊 Strength:\n ' + unit[1]['strength'] + '\n\n😖 Weakness:\n ' + unit[1]['weakness']

    print("**********************************************")
    print("Couldn't find unit!")
    print("Unit supplied:" + user_supplied_unit_name)
    print("**********************************************")

    return '😔 **I couldn\'t find that unit sire.** I have recorded your message to study it. I will update the scrolls if required. Try typing "!help". '
