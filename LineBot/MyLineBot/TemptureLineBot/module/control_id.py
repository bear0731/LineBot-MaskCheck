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
                pass            
            else:
                self.jdata["allUserId"].append(id)                
                

            #   add name in staffName
            if  name in self.jdata["group"][group]["staffName"]:
                pass            
            else:
                self.jdata["group"][group]["staffName"].append(name)                
                

            #   add id in staffId
            if  id in self.jdata["group"][group]["staffId"]:
                pass            
            else:
                self.jdata["group"][group]["staffId"].append(id) 

            json.dump(self.jdata,jfile,indent=4)
            
        