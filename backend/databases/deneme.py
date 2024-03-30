from mongo_process import operation_mongo
from bson import objectid

#Sinan Uyğun hesabı
accounts="mongodb+srv://sinanuygun:BnKJOKx7OTvSWLfD@eternalib.06ijzom.mongodb.net/?retryWrites=true&w=majority&appName=eternaLib"
#Emre Yörük Hesabı
accounte="mongodb+srv://emreyoruk:VD9qAxtJKPCrkPTq@eternalib.06ijzom.mongodb.net/?retryWrites=true&w=majority&appName=eternaLib"
#Onur Karakaya hesabı
accounto="mongodb+srv://onurkarakaya:rGc9zx2kOzLOtBM5@eternalib.06ijzom.mongodb.net/?retryWrites=true&w=majority&appName=eternaLib"

# process_mongo sınıfını kullanarak MongoDB işlemleri gerçekleştirme
mng = operation_mongo(accounts)

h=mng.get_id("mgb_data","movie")
print(h)
t=mng.search_id("mgb_data","movie","660425841b5299643632ef48")
print(t)

# Bağlantıyı kapat
mng.close()
