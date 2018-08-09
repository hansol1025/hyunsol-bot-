import discord
import asyncio
import random
import pickle
import os

client = discord.Client()

@client.event
async def on_ready():
	print("ONLINE! Hyunsol!")

@client.event
async def on_message(message):
	if message.content.startswith('테스트'):
		await client.send_message(message.channel, '안녕!')

client.run(os.getenv('TOKEN'))
