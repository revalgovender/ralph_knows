import json
import os
import discord


def get_response(message: str, username: str):
    user_supplied_unit_name = message.lower()
    file = open('data/units.json')
    data = json.load(file)

    for unit in data.items():
        if user_supplied_unit_name in unit[1]['aliases']:

            counters = unit[1]['weakness']

            if counters[-1] == '.':
                counters = counters.rstrip(counters[-1])

            embed = discord.Embed(title=counters, description="are the counters for " + unit[1]['actual-name'],
                                  color=0x9a8da7)
            return embed

    embed = discord.Embed(title="😔 I couldn't find that unit sire",
                          description='I have recorded your message to study it. I will update the scrolls if required.',
                          color=0xf22c56)
    return embed


def get_civ_data(message: str, username: str):
    user_supplied_civ_name = message.lower()
    file = open('data/civs.json')
    data = json.load(file)

    for civ in data.items():
        civ_name = civ[1]['name']
        civ_name = civ_name.lower()
        if user_supplied_civ_name in civ_name:
            strengths = civ[1]['strengths']
            strengths = ', '.join(strengths)
            strengths = strengths.capitalize()
            build = civ[1]['build']
            build = ', '.join(build)
            civ_name = civ[1]['name']

            embed = discord.Embed(title="", description="", color=0x9a8da7)
            embed.set_author(name=civ_name, icon_url="https://aoecompanion.com/civ-icons/" + civ_name.lower() + '.png')
            embed.add_field(name='Have strong', value=strengths, inline=False)
            embed.add_field(name='Try building', value=build, inline=False)
            return embed

    embed = discord.Embed(title="😔 I couldn't find that civ sire",
                          description='I have recorded your message to study it. I will update the scrolls if required.',
                          color=0xf22c56)
    return embed


def get_build_order_response(type: int):
    instructions = []
    title = ''

    if type == 1:
        title = '🐎 Generic Knight Rush'
        instructions = [
            "First 3 villagers build houses and then harvest sheep",
            "6 sheep.",
            "7 build lumber camp",
            "7, 8 and 9th villager chop wood.",
            "10 villager builds house and lures boar.",
            "11 and 12 villager chop wood.",
            "13 villager builds mill on berries.",
            "13, 14, 15 harvest berries.",
            "16 lures boar.",
            "17 builds house then harvest berries.",
            "18, 19 berries",
            "20 builds house and then a lumber camp in another wood line(this is important)",
            "21, 22, 23, 24 to wood in new lumber camp.",
            "25 builds mining camp.",
            "26, 27 gold.",
            "Research Feudal Age.",
            "One of villagers in wood builds barracks.",
            "Villager 28, 29 mine gold.",
            "One of wood villagers builds blacksmith and stable.",
            "Research Castle age.",
            "While going to castle research available technologies at lumber camp and mill.",
            "2 Knights at your stable and attack!",
        ]

    if type == 2:
        title = '⚔️ Rev Man-at-Arms Rush'
        instructions = [
            "First 3 villagers build houses and then harvest sheep",
            "6 sheep.",
            "7 build lumber camp",
            "7, 8 and 9th villager chop wood.",
            "10 villager builds house and lures boar.",
            "11 and 12 villager chop wood.",
            "13 villager builds mill on berries.",
            "13, 14, 15 harvest berries.",
            "16 lures boar.",
            "17 builds house then harvest berries.",
            "18, 19 gold",
            "20 berries",
            "21 stone",
        ]

    embed = discord.Embed(title=title, description='', color=0x9a8da7)

    for instruction in instructions:
        embed.add_field(name='', value='- ' + instruction, inline=False)

    return embed
