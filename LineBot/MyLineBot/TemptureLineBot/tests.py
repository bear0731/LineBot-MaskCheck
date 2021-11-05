from django.test import TestCase
import json
import os
with open(os.path.join(os.getcwd(),".\LineBot\\MyLineBot\\TemptureLineBot\\static\\UserInformation.json"),'r',encoding='utf8') as jfile:
    data = json.load(jfile)
group=input()
output = data["group"][group]["staff"][0]
print(output)           