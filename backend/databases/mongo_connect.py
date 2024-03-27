import pymongo 

class databases:
    def __init__(self) -> None:
        pass

    def connect(self,account:str)->list:
        myclient= pymongo.MongoClient(account)
        return myclient


account="mongodb+srv://sinanuygun:BnKJOKx7OTvSWLfD@eternalib.06ijzom.mongodb.net/?retryWrites=true&w=majority&appName=eternaLib"
db=databases()
myclient=db.connect(account) 
print(myclient.list_database_names())