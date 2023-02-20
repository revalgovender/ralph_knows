import json
import os
import discord


def get_response(message: str, username: str):
    user_supplied_unit_name = message.lower()

    if user_supplied_unit_name == 'hello':
        return 'Hey there!'

    file = open('data/units.json')
    data = json.load(file)

    for unit in data.items():
        if user_supplied_unit_name in unit[1]['aliases']:
            embed = discord.Embed(title="⚔️ Counter to " + unit[1]['actual-name'], description=unit[1]['weakness'], color=0x9a8da7)
            return embed

    log_failed_request(user_supplied_unit_name, username)

    embed = discord.Embed(title="😔 I couldn't find that unit sire", description='I have recorded your message to study it. I will update the scrolls if required.', color=0xf22c56)
    return embed


def log_failed_request(user_supplied_unit_name, username):
    # Read log file.
    log = 'data/failed-requests.json'
    with open(log) as logfile:
        failed_requests = json.load(logfile)

    # Add new failed request.
    new_failed_request = {
        'username': username,
        'unit_name_supplied': user_supplied_unit_name,
    }
    failed_requests.append(new_failed_request)
    failed_requests = json.dumps(failed_requests, indent=2)

    # Update log file.
    with open(log, "w") as outfile:
        outfile.write(failed_requests)
