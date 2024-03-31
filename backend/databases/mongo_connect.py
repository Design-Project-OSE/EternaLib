from flask import Flask, jsonify
import pymongo
from mongo_process import operation_mongo

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
accounte="mongodb+srv://emreyoruk:VD9qAxtJKPCrkPTq@eternalib.06ijzom.mongodb.net/"
#Onur Karakaya hesabı
accounto="mongodb+srv://onurkarakaya:rGc9zx2kOzLOtBM5@eternalib.06ijzom.mongodb.net/?retryWrites=true&w=majority&appName=eternaLib"

db=databases(accounts) #accounts yerine kendi hesabınızı kullanabilirsiniz

liste=db.getbase() #database isimlerini veriyor
print(liste)

collec=db.getcol("mgb_data","movie",True)#collection (movie) içeriğini veriyor
print(collec)

print("------------------------------emre----------------------")
mng = operation_mongo(accounts)


#-------------------------------------------------------------------------------------
h=mng.get_id("mgb_data","movie")
d = [str(x) for x in h]
print(mng.find_data("mgb_data","movie","_id",h[0]))

#-------------------------------------------------------------------------------------

head=db.gethead("mgb_data","movie","name")#herhangi bir içeriği çekmeni sağlıyor (sadece name'leri çekiyor)
print(head)

db.close()

app = Flask(__name__)

@app.route('/movies', methods=['GET'])
def get_data():
    return jsonify(collec)

@app.route('/detail/<id>', methods=['GET'])
def get_movie(id):
    for x in d:
        a = mng.find_data("mgb_data","movie","_id",h[x])
        if(x) == str(id):
            return jsonify(a)
        
        return "hello"


if __name__ == '__main__':
    app.run()