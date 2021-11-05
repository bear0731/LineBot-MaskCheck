import json
import os
class manageUserInformation():

    def __init__(self): #read all of user informaion data
        with open(os.path.join(os.getcwd(),".\TemptureLineBot\\static\\UserInformation.json"),'r',encoding='utf8') as jfile:
            self.jdata = json.load(jfile)
        
    def getAllId(self): #return everybody id
        return self.jdata["allUserId"]
    
    def addInformation(self,id,name,group):#store new id
        with open(os.path.join(os.getcwd(),".\TemptureLineBot\\static\\UserInformation.json"),'w',encoding='utf8') as jfile:

            #   add id in allId
            if  id in self.jdata["allUserId"]:
                json.dump(self.jdata,jfile,indent=4)            
            else:
                self.jdata["allUserId"].append(id)                
                json.dump(self.jdata,jfile,indent=4)

            #   add name in staffName
            if  name in self.jdata["group"][group]["staffName"]:
                json.dump(self.jdata,jfile,indent=4)            
            else:
                self.jdata["group"][group][name].append(name)                
                json.dump(self.jdata,jfile,indent=4)

            #   add id in staffId
            if  id in self.jdata["group"][group]["staffId"]:
                json.dump(self.jdata,jfile,indent=4)            
            else:
                self.jdata["group"][group][id].append(id)                
                json.dump(self.jdata,jfile,indent=4)
            
        