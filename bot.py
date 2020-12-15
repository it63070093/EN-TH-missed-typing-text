import discord
import asyncio
from discord.ext import commands
from langdetect import DetectorFactory
DetectorFactory.seed = 0
import langdetect as ld
from ENTH import en2th_text, enth_main
client = commands.Bot(command_prefix='-') #กำหนด Prefix

@client.event
async def on_ready() : #เมื่อระบบพร้อมใช้งาน
    print(client.user.name + ' is Online...') #แสดงผลใน CMD

@client.event
async def on_message(message) : #ดักรอข้อความใน Chat
    msg = message.content
    if msg[0:2] == '-t':
        tmessage = enth_main(msg[2:])

        await message.channel.send(tmessage)
    elif msg == 'Hello' or msg == 'hello':
        await message.channel.send("สวัสดีครับท่านสมาชิกชมรมคนชอบ PSIT")
    elif msg == 'Help' or msg == 'help':
        await message.channel.send("Use -t 'your text' to convert into another language.(EN/TH)")
    else:
         pass

TOKEN = 'NzgxMzg0NjMwNTE5NTk1MDY4.X783JQ.47UiovzVixVdvMT3VHG48k5ofno'
client.run(TOKEN) #รันบอท (โดยนำ TOKEN จากบอทที่เราสร้างไว้นำมาวาง)