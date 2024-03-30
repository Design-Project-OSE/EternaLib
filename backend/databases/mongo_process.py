import pymongo 
from bson import objectid
        
class operation_mongo:
    def __init__(self,account) -> None:
        self.myclient=operation_mongo.connect(account)
       
    @staticmethod    
    def connect(account:str)->pymongo.MongoClient:
        """
        [en]The function must contain a link for mongo access: accounts=mongodb+srv://<username>:<password>@eternalib.06ijzom.mongodb.net/?retryWrites=true&w=majority&appName=eternaLib 
        The function returns the mongoclient value.
        
        [tr]Fonksiyon mongo erişim için bir link içermelidir: accounts=mongodb+srv://<username>:<password>@eternalib.06ijzom.mongodb.net/?retryWrites=true&w=majority&appName=eternaLib 
        Fonksiyon mongoclient değeri döndürmektedir.
        """
        myclient= pymongo.MongoClient(account)
        return myclient
    
    def pull_collection(self, name_database: str,name_collection:str,no_id:bool) -> list:
        nclient=self.myclient[name_database]
        ncollection=nclient[name_collection]
        if no_id:    
            result=ncollection.find({},{"_id":0})
        else:
            result=ncollection.find()
        res_list=[]
        for item in result:
            res_list.append(item)
        return res_list
    
    def pull_database(self)->list:
        cname=self.myclient.list_database_names()
        res_list=[]
        for item in cname:
            res_list.append(item)
        return res_list
    
    def pull_head(self,name_database:str,name_collection:str,name_head:str)->list:
        nbase=self.myclient[name_database]
        ncollection=nbase[name_collection]
        nhead=ncollection.find({},{name_head:1,"_id":0})
        result=[item[name_head] for item in nhead]
        return result
    
    def write_data(self,name_database,name_collection,add_data)->None: 
        """
        [en]The data to be received by the function must be in the following format: {"name": Owl,"type":animal...} 
        You can enter as much data as you want to the function.
        
        [tr]Fonksiyonun alacağı veriler şu formatta olmalı: {"name": Owl,"type":animal...} 
        Fonksiyona name_database: kaydedileceği database ismi
        name_collectin: kaydedileceği collection ismi
        add_data: {} ile tanımlanmış uygun formatta json verisi
        """
        nbase=self.myclient[name_database]
        ncollection=nbase[name_collection]
        n_id=ncollection.insert_one(add_data)
        return n_id        
    
    def delete_data(self,name_database:str,name_collection:str,_id:str)->None:
        nbase=self.myclient[name_database]
        ncollection=nbase[name_collection]
        delete_data = {"_id": objectid(_id)}
        n_id=ncollection.delete_one(delete_data)
        return n_id
        
    def find_data(self, name_database, name_collection,search_type,search_word: str, filter="all", no_id=False) -> dict:
        nbase = self.myclient[name_database]
        ncollection = nbase[name_collection]
        peace={search_type:search_word}
        
        projection = {"_id": 0} if no_id else {}  # varsayılan olarak _id'yi gösterme
        if filter != "all":
            projection[filter] = 1  # filtre belirtilmişse, sadece belirtilen alanı göster
        
        result = ncollection.find_one(peace, projection)
        
        return result
    

    def close(self):
        """
        [en]Disconnects the connection with Mongo
        [tr] Mongo ile olan bağlantıyı keser
        """
        self.myclient.close()
    
        
        



