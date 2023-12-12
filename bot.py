import discord
from discord.ext.commands import bot

import responses
import classes

output_channel_ID = ''


async def send_message(client, username, message, user_message, is_private):
    try:
        bot_channel = client.get_channel(1175203861145849969)
        response = responses.get_response(username, user_message)
        await bot_channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = ''
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

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

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            print(username)
            if channel == 'Direct Message with Unknown User':
                print('channel found')

                await send_message(client, username, message, user_message, is_private=True)
            else:
                await send_message(client, username, message, user_message, is_private=False)
        else:
            return

    client.run(TOKEN)
