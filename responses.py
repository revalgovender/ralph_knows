import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if p_message == '!help':
        return '`This is a help message that you can modify.`'

    if p_message == 'militia':
        return 'Archers'

    if p_message == 'man-at-arms' or p_message == 'Man at arms':
        return 'Archers and Scorpions'

    if p_message == 'long swordsman':
        return 'Archers and Scorpions'

    if p_message == 'two-handed swordsman':
        return 'Archers and Scorpions'

    if p_message == 'champion':
        return 'Archers and scorpions'

    if p_message == 'spearman':
        return 'Archers and other infantry'

    if p_message == 'pikeman':
        return 'Archers, scorpions and other infantry'

    if p_message == 'halberdier':
        return'Archers, scorpions and other infantry'

    if p_message == 'eagle scout':
        return 'Infantry'

    if p_message == 'eagle warrior':
        return 'Infantry'

    return 'I didn\'t understand what you wrote. Try typing "!help".'
