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
		chat = random.choice(['안녕!', 'ㅎㅇㅎㅇ', '반가워', '안녕', '왜 왔어!', '그래', 'ㅇㅇ', '응', '왜이리 늦었어', '어디 갔다 옴?'])
		await client.send_message(message.channel, chat)
	if message.content.startswith('현솔아 몇살이야'):
		chat = random.choice(['안녕 나는 열두살이야', '반가워 나는 12살이야 초5 임', '초5 인데', '12!', '열두살', '12', '초등학교 5학년인데', '12살이다, 왜!', '곧있으면 13살이다!!', '꼭 말해줘야 하나..'])
		await client.send_message(message.channel, chat)
	if message.content.startswith('현솔아 뭐해'):
		chat = random.choice(['그러게 나도 지금 내가 뭘하고 있는지 모르겠어', '유튜브 보는중임', '음악 듣는중..', 'TV 앞에서 핸드폰하는중..', '하이픽셀 에서 5연패 하는중..!', '참교육중!', '학원이다 말걸지 마라;', '아무거나', '부르지 마삼', '부르지마', '비밀 ㅋ', '하이픽셀에서 TNTT 런 하고 있는데요', '좀비고하는중임', '좀비스중..', '밥좀먹자', '유튜브 보는중이니까 말걸지마삼', '왜 또', '나한테 IM 자제좀;', '누군가랑 노느중', '빨간토마토 영상 보는중', '배그하는데 바아해하지 마셈;', '아르카에서 다구리 당하는중', '너님이 알거 없잖아요 ㅋ', '모니터 화면 보고 있는데', '약속있어서 놀다 오는중', '엄청난 것을 하고 있어', 'Flux 으로 핵쓰는중 Vape는 어떻게 쓰는지 모르겠더라;', '누군가를 ])
		await client.send_message(message.channel, chat)
	if message.content.startswith('현솔아 몇살이야'):
		chat = random.choice(['안녕 나는 열두살이야', '반가워 나는 12살이야 초5 임', '초5 인데', '12!', '열두살', '12', '초등학교 5학년인데', '12살이다, 왜!', '곧있으면 13살이다!!', '꼭 말해줘야 하나..'])
		await client.send_message(message.channel, chat)
	if message.content.startswith('현솔아 몇살이야'):
		chat = random.choice(['안녕 나는 열두살이야', '반가워 나는 12살이야 초5 임', '초5 인데', '12!', '열두살', '12', '초등학교 5학년인데', '12살이다, 왜!', '곧있으면 13살이다!!', '꼭 말해줘야 하나..'])
		await client.send_message(message.channel, chat)
				      
client.run(os.getenv('TOKEN'))
