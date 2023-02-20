import discord
import src.responses as responses
import os


async def send_message(message, user_message, username, is_private):
    try:
        response = responses.get_response(user_message, username)
        await message.author.send(embed=response) if is_private else await message.author.send(embed=response)

    except Exception as e:
        print(e)


def run_discord_bot():
    token = os.environ['TOKEN']
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, username, is_private=True)
        else:
            await send_message(message, user_message, username, is_private=False)

    client.run(token)