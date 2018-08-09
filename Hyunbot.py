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
	if message.content.startswith('안녕'):
		chat = random.choice(['안녕!', 'ㅎㅇㅎㅇ', '반가워', '안녕', '왜 왔어!, '그래, 'ㅇㅇ', '응', '왜이리 늦었어', '어디 갔다 옴?'])
		await client.send_message(message.channel, chat)
	if message.content.startswith('현솔아 몇살이야'):
		chat = random.choice(['안녕 나는 열두살이야', '반가워 나는 12살이야 초5 임', '반가워', '안녕', '왜 왔어!, '그래, 'ㅇㅇ', '응', '왜이리 늦었어', '어디 갔다 옴'
		await client.send_message(message.channel, '안녕!')
				      
client.run(os.getenv('TOKEN'))
