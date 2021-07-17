import discord
import os
from asyncio import sleep

client = discord.Client()

@client.event
#起動時処理
async def on_ready():
    for channel in client.get_all_channels():
        print("----------")
        print("チャンネル名：" + str(channel.name))
        print("チャンネルID：" + str(channel.id))
        print("----------")


@client.event
#メッセージを受け取って起動
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '/neko':
        await message.channel.send('にゃーん')

    #強制切断bot
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

            message.guild.voice_client.play(discord.FFmpegPCMAudio('逃げたほうがいいかもね.wav'))
            while message.guild.voice_client.is_playing():
                await sleep(0.1)
            for member in message.author.voice.channel.members:
                await member.move_to(None)
            await message.guild.voice_client.disconnect()
            return

        await message.channel.send("アルティメットはまだ！")
"""
@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        botRoom = client.get_channel(os.environ["CHANNEL_ID"])
        voiceChannelIds = [vc for vc in client.get_all_channels().id if ]
"""


client.run(os.environ["DISCORD_TOKEN"])
