#LINE Bot接收訊息後，所要執行的運算邏輯
from os import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import Settings, settings
import json
from linebot import LineBotApi, WebhookParser
from linebot import models
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, messages
from linebot.models.events import FollowEvent, UnfollowEvent
from linebot.models.send_messages import SendMessage
from linebot.models.sources import Source
# from LineBot.MyLineBot.TemptureLineBot.module.Follow_event import follow
from TemptureLineBot.module.control_id import manageUserInformation
from TemptureLineBot.module.Follow_event import follow
from TemptureLineBot.module.connectcall import connectcall

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
id=settings.LINE_CHANNEL_ID
MUI = manageUserInformation()
CC=connectcall()
@csrf_exempt
def callback(request):
    
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent): #學使用者說話                 
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))    
                s=event.message.text
                
                if("!登記" in s):                      
                        a=s.split("\n")
                        a=a[1].split(",")
                        group=a[0]
                        name=a[1]
                        id=event.source.user_id
                        print(id)
                        MUI.addInformation(id,name,group)
                if("!分機號碼" in s):                      
                    s=CC.show_number()
                    print(s)
            # elif isinstance(event,FollowEvent): #請使用者回傳服務部門以及姓名
            #     follow.replay(event)
            #     MUI.addInformation()


            elif isinstance(event,UnfollowEvent): # unfollow沒有replyToken
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="bad"))
                   
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


