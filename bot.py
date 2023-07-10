import os

import discord
import responses
from dotenv import load_dotenv

load_dotenv()


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(embed=response) if is_private else await message.channel.send(embed=response)

    except Exception as e:
        pass


def run_discord_bot():
    intent = discord.Intents.default()
    intent.message_content = True
    client = discord.Client(intents=intent)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: {user_message} in channel: {channel}')

        if user_message is None or len(user_message) == 0:
            return

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(os.getenv('TOKEN'))
