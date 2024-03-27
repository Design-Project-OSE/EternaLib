import pymongo 

class databases:
    def __init__(self,account) -> None:
        self.myclient=databases.connect(account)

    # database bağlantısı oluşturuyor
    def connect(account:str)->pymongo.MongoClient:
        myclient= pymongo.MongoClient(account)
        return myclient
    
    def getcol(self, base: str,collection:str,no_id:bool) -> list:
        nclient=self.myclient[base]
        ncollec=nclient[collection]
        if(no_id==True):    
            result=ncollec.find({},{"_id":0})
        else:
            result=ncollec.find()
        res_list=[]
        for item in result:
            res_list.append(item)
        return res_list
    
    def getbase(self)->list:
        cname=self.myclient.list_database_names()
        res_list=[]
        for item in cname:
            res_list.append(item)
        return res_list
    
    def gethead(self,base:str,collection:str,head:str)->list:
        nbase=self.myclient[base]
        ncollection=nbase[collection]
        nhead=ncollection.find({},{head:1,"_id":0})
        result=[item[head] for item in nhead]
        return result
    
    def close(self):
        self.myclient.close()
        
        

#Sinan Uyğun hesabı
accounts="mongodb+srv://sinanuygun:BnKJOKx7OTvSWLfD@eternalib.06ijzom.mongodb.net/?retryWrites=true&w=majority&appName=eternaLib"
#Emre Yörük Hesabı
accounte="mongodb+srv://emreyoruk:Mipym9mZgEn3raJm@eternalib.06ijzom.mongodb.net/"
#Onur Karakaya hesabı
accounto="mongodb+srv://onurkarakaya:tCPSdNsx6MQWOzOc@eternalib.06ijzom.mongodb.net/"

db=databases(accounts) #accounts yerine kendi hesabınızı kullanabilirsiniz

liste=db.getbase() #database isimlerini veriyor
print(liste)

collec=db.getcol("mgb_data","movie",True)#collection içeriğini veriyor
print(collec)

head=db.gethead("mgb_data","movie","title")#herhangi bir içeriği çekmeni sağlıyor
print(head)

db.close()

