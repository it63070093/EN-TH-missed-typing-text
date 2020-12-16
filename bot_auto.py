import discord
from discord.ext import commands
from langdetect import DetectorFactory
DetectorFactory.seed = 0
import langdetect as ld
from ENTH import enth_main
client = commands.Bot(command_prefix='-') #กำหนด Prefix

@client.event
async def on_ready() : #เมื่อระบบพร้อมใช้งาน
    print(client.user.name + ' is Online...') #แสดงผลใน CMD

@client.event
async def on_message(message) : #ดักรอข้อความใน Chat
    if message.author == client.user:
        return
    msg = message.content
    if msg == '-Help' or msg == '-help' or msg == "-HELP":
        await message.channel.send("If you type something you didn't mean to, i'll correct it.")
    if msg[0] == '@' or msg.isnumeric() == True or msg.isspace() == True or msg.isdecimal() == True:
        return
    if 'https://www.' in msg or 'www.' in msg:
        return
    if msg in open('thai_dict.txt', encoding="utf8").read():
        return
    if msg.upper() in open('dictionary.txt').read():
        return
    if msg.isascii() == True or ld.detect(msg) == 'th':
        tmessage = enth_main(msg)
        mention = str(message.author.mention)
        await message.channel.send(mention+' said "' + tmessage + '".')
    else:
        return

TOKEN = 'NzgxMzg0NjMwNTE5NTk1MDY4.X783JQ.ArHDvVzyN7vjiqUE3ehEo2Y2aeA'
client.run(TOKEN) #รันบอท (โดยนำ TOKEN จากบอทที่เราสร้างไว้นำมาวาง)