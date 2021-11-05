from linebot import LineBotApi
from django.conf import Settings, settings
from linebot.models import MessageEvent, TextSendMessage, messages
from .control_id import manageUserInformation
class follow():
    def __init__(self):
       self.line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
        
    def replay(self,event):
         grouping_text="你好，恭喜您已成功加入本公司的功能整合系統,\n請您輸入您在本公司負責的部門\nex:(請依照格輸入)\n網路行銷,王小明"
         self.line_bot_api.reply_message(event.reply_token,TextSendMessage(grouping_text))
         
#是否可以做成訊息網:
#ex
#程式部:1,實體行銷部:2,網路行銷部:3,包裝部:4
    

        

    
