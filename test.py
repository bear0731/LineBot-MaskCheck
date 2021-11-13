import json
import os
with open('.\\a.json','r',encoding='utf8') as f:
    jdata=json.load(f)
    for i in jdata["group"]:
        print(i)

