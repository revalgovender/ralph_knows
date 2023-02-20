from discord import app_commands
import discord
import os

from src import responses

if __name__ == '__main__':
    class Ralph(discord.Client):
        def __init__(self):
            super().__init__(intents=discord.Intents.default())
            self_synced = False

        async def on_ready(self):
            try:
                print('trying to sync')
                synced = await tree.sync(guild=discord.Object(id=521077625519603712))
                print(f"Synced {len(synced)} commands.")
                self_synced = True
            except Exception as exception:
                print(exception)
            print(f'{bot.user} is now running!')


    bot = Ralph()
    tree = app_commands.CommandTree(bot)


    @tree.command(name='counter', description='Get counter to Age of Empires 2 DE unit.',
                  guild=discord.Object(id=521077625519603712))
    @app_commands.describe(unit="What unit do you need the counter for?")
    async def self(interaction: discord.Interaction, unit: str):
        response = responses.get_response(unit, str(interaction.user))
        await interaction.response.send_message(embed=response, ephemeral=False)


    bot.run(token=os.environ['TOKEN'])
