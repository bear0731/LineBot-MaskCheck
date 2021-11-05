from django.conf import settings
import requests
import serial
from linebot import LineBotApi, WebhookParser
import json

from LineBot.MyLineBot.TemptureLineBot.module.control_id import manageUserInformation
from LineBot.MyLineBot.MyLineBot.settings import LINE_CHANNEL_ACCESS_TOKEN
from linebot.models import MessageEvent, TextSendMessage
import os
comPort="COM3"
baudRate=9600
si=serial.Serial(comPort,baudRate)

with open(os.path.join(os.getcwd(),".\LineBot\\MyLineBot\\TemptureLineBot\\static\\UserInformation.json"),'r',encoding='utf8') as jfile:
        jdata = json.load(jfile)
        all_id=jdata["allUserId"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

while True: 
    if si.in_waiting:
        s=si.readline().decode('utf-8').replace("\n","")
        line_bot_api.multicast(all_id, TextSendMessage(text='{}'.format(s)))


