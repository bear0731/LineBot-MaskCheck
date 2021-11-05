#LINE Bot接收訊息後，所要執行的運算邏輯
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import Settings, settings
import json
from linebot import LineBotApi, WebhookParser
from linebot import models
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, messages
from linebot.models.events import FollowEvent
from linebot.models.send_messages import SendMessage
from linebot.models.sources import Source
# from LineBot.MyLineBot.TemptureLineBot.module.Follow_event import follow
from TemptureLineBot.module.control_id import manageUserInformation
from TemptureLineBot.module.Follow_event import follow


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
id=settings.LINE_CHANNEL_ID
MUI = manageUserInformation()

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
            if isinstance(event, MessageEvent):  
                
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))               
            elif isinstance(event,FollowEvent):
                follow.replay(event)
                MUI.addInformation()
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
@csrf_exempt
def helpme(request):
    print("hi")


