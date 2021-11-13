import os
import json
class connectcall():
    def __init__(self) -> None:
        with open(os.path.join(os.getcwd(),".\TemptureLineBot\\static\\UserInformation.json"),'r',encoding='utf8') as jfile:
            self.jdata = json.load(jfile)
    def show_number(self):
        c=1
        s=""
        s+="第一碼為部門，第二碼為職位，接著使用\":\"來傳達你想對此目標說的話\n"
        s+="第一碼:\n"
        for i in self.jdata["group"]:
            s+=(f"部門分機{c}為:{i}\n")
            c+=1
        return s
        


    
    
