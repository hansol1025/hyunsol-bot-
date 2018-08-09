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
	if message.content.startswith('현솔아 바보'):
		chat = random.choice(['뭐', 'ㅋ', '어쩌라는 건지;', '님부터 생각하시죠?', '아무것도 안한 사람한테 화풀이 하네;', '바보라고 하는 사람이 바보랬어요', '님 인성부터 고치고.. 크흠', '초딩이라고 무시하는거임?', '님보다 아는거 많은데 ㅋ', '하하;', '그래서 뭐', '불만 있냐', '하..', '재밋냐', '어이가 없네', '밥먹고 있는 사람한테 할말 인가;', '님부터 생각하세요^^', '내가 바보라면 이 세상에 있는 모든 디스코드 봇들도 바보인거야', '논리적으로 말해보시져', '내가 어째서 바보라는 거죠?', '초면에 예의가 없네요 ㅋ', '누구세요 ㅋ', '님보단 수학 잘하는데 ^^', '말하는이의 인성이 좋지 않다면 입 다뭅시다', '안 재밌음', '안물어봤는데..', '내가 바보라는 근거 있나요? 만약 있다면 근거를 100가지 이상 말해보세요 ^^', 'ㅋ 수준떨어지는 놈', '안궁금함 내가 바보인지 뭔지는 님보다 내가 더 잘알음 ㅋ', '님이 나를 바보라고 하는건 엄청난 실례인건 아시죠? 남이사 바보이든 말든 뭔상관이죠?'])
		await client.send_message(message.channel, chat)
	if message.content.startswith('현솔아 몇살이야'):
		chat = random.choice(['안녕 나는 열두살이야', '반가워 나는 12살이야 초5 임', '초5 인데', '12!', '열두살', '12', '초등학교 5학년인데', '12살이다, 왜!', '곧있으면 13살이다!!', '꼭 말해줘야 하나..'])
		await client.send_message(message.channel, chat)
				      
client.run(os.getenv('TOKEN'))
