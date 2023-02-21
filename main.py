import json
import typing
import random

from discord import app_commands
import discord
import os
from typing import List

from src import responses

if __name__ == '__main__':
    class Ralph(discord.Client):
        def __init__(self):
            super().__init__(intents=discord.Intents.default())
            self_synced = False

        async def on_ready(self):
            try:
                # print('trying to sync')
                # synced = await tree.sync(guild=discord.Object(id=521077625519603712))
                # print(f"Synced {len(synced)} commands.")
                self_synced = True
            except Exception as exception:
                print(exception)
            print(f'{bot.user} is now running!')


    bot = Ralph()
    tree = app_commands.CommandTree(bot)


    async def unit_autocomplete(
            interaction: discord.Interaction,
            current: str,
    ) -> typing.List[app_commands.Choice[str]]:
        units = []
        file = open('data/units.json')
        data = json.load(file)

        for unit in data.items():
            units.append(unit[1]['actual-name'].lower())

        # Create random 5 units to display before using starts typing unit.
        # This will prevent Discord trying to grab the entire list of units.
        if not current:
            short_unit_list = random.sample(units, 5)
            return [
                app_commands.Choice(name=short_unit_list[0], value=short_unit_list[0]),
                app_commands.Choice(name=short_unit_list[1], value=short_unit_list[1]),
                app_commands.Choice(name=short_unit_list[2], value=short_unit_list[2]),
                app_commands.Choice(name=short_unit_list[3], value=short_unit_list[3]),
                app_commands.Choice(name=short_unit_list[4], value=short_unit_list[4]),
            ]

        # Perform filtering to limit list to items which match user input.
        # We do this because Discord only allows a max of 25 autocomplete results.
        # Thankfully we don't need any other limitations here as we don't have that many units.
        units = [i for i in units if i.startswith(current)]

        return [
            app_commands.Choice(name=unit, value=unit)
            for unit in units if current.lower() in unit.lower()
        ]


    @tree.command(name='counter', description='Get unit counter',
                  guild=discord.Object(id=521077625519603712))
    @app_commands.describe(unit="What unit do you need the counter for?")
    @app_commands.autocomplete(unit=unit_autocomplete)
    async def self(interaction: discord.Interaction, unit: str):
        response = responses.get_response(unit, str(interaction.user))
        await interaction.response.send_message(embed=response, ephemeral=False)


    @tree.command(name='build-order', description='Get build order',
                  guild=discord.Object(id=521077625519603712))
    @app_commands.describe(types="Build orders available")
    @app_commands.choices(types=[
        discord.app_commands.Choice(name='Generic Knight rush', value='1'),
        discord.app_commands.Choice(name='Rev Man-at-Arms rush', value='2'),
    ])
    async def self(interaction: discord.Interaction, types: discord.app_commands.Choice[str]):
        response = responses.get_build_order_response(int(types.value))
        await interaction.response.send_message(embed=response, ephemeral=False)

    async def civ_autocomplete(
            interaction: discord.Interaction,
            current: str,
    ) -> typing.List[app_commands.Choice[str]]:
        civs = []
        file = open('data/civs.json')
        data = json.load(file)

        for civ in data.items():
            civs.append(civ[1]['name'].lower())

        # Create random 5 civs to display before using starts typing civ.
        # This will prevent Discord trying to grab the entire list of civs.
        if not current:
            short_civ_list = random.sample(civs, 5)
            return [
                app_commands.Choice(name=short_civ_list[0], value=short_civ_list[0]),
                app_commands.Choice(name=short_civ_list[1], value=short_civ_list[1]),
                app_commands.Choice(name=short_civ_list[2], value=short_civ_list[2]),
                app_commands.Choice(name=short_civ_list[3], value=short_civ_list[3]),
                app_commands.Choice(name=short_civ_list[4], value=short_civ_list[4]),
            ]

        # Perform filtering to limit list to items which match user input.
        # We do this because Discord only allows a max of 25 autocomplete results.
        # Thankfully we don't need any other limitations here as we don't have that many civs.
        civs = [i for i in civs if i.startswith(current)]

        return [
            app_commands.Choice(name=civ, value=civ)
            for civ in civs if current.lower() in civ.lower()
        ]


    @tree.command(name='civ', description='Get civ data',
                  guild=discord.Object(id=521077625519603712))
    @app_commands.describe(civ="What civ do you want information about?")
    @app_commands.autocomplete(civ=civ_autocomplete)
    async def self(interaction: discord.Interaction, civ: str):
        response = responses.get_civ_data(civ, str(interaction.user))
        await interaction.response.send_message(embed=response, ephemeral=False)

# bot.run(token=os.environ['TOKEN'])
bot.run(token='MTA3NjQ0ODU0MjIwMzMzNDY4Ng.G-yaPF.C2OLf9z52J9uHaScc41qdwB9FQtm3n7FV6EJI8')
