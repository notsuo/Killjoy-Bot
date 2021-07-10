import discord
import os
from asyncio import sleep

client = discord.Client()

"""
if not discord.opus.is_loaded():
    discord.opus.load_opus("heroku-buildpack-libopus")
    """

@client.event
async def on_ready():
    for channel in client.get_all_channels():
        print("----------")
        print("チャンネル名：" + str(channel.name))
        print("チャンネルID：" + str(channel.id))
        print("----------")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '/neko':
        await message.channel.send('にゃーん')

    if message.content == '!kj ult':

        if message.author.voice is None:
            await message.channel.send("アルティメット準備中")
            return

        if message.guild.voice_client is None:
            await message.author.voice.channel.connect()

            for member in message.author.voice.channel.members:
                if member.bot:
                    continue

                await message.channel.send(member.mention)

            message.guild.voice_client.play(discord.FFmpegPCMAudio('YouShouldRun.mp3'))
            print(str(message.guild.voice_client.is_playing()))
            while message.guild.voice_client.is_playing():
                await sleep(1)
            for member in message.author.voice.channel.members:
                await member.move_to(None)

            await message.guild.voice_client.disconnect()
            return

        await message.channel.send("アルティメットはまだ！")


client.run(os.environ["DISCORD_TOKEN"])
