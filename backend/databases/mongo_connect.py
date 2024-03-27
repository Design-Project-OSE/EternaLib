import pymongo 

class databases:
    def __init__(self) -> None:
        pass

    # database bağlantısı oluşturuyor
    def connect(self,account:str)->pymongo.MongoClient:
        myclient= pymongo.MongoClient(account)
        return myclient


accounts="mongodb+srv://sinanuygun:BnKJOKx7OTvSWLfD@eternalib.06ijzom.mongodb.net/?retryWrites=true&w=majority&appName=eternaLib"
accounte="mongodb+srv://emreyoruk:Mipym9mZgEn3raJm@eternalib.06ijzom.mongodb.net/"
accounto="mongodb+srv://onurkarakaya:tCPSdNsx6MQWOzOc@eternalib.06ijzom.mongodb.net/"
db=databases()
myclient=db.connect(accounto) 
print(accounto)
print(myclient.list_database_names())