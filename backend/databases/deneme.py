from mongo_process import operation_mongo

#Sinan Uyğun hesabı
accounts="mongodb+srv://sinanuygun:BnKJOKx7OTvSWLfD@eternalib.06ijzom.mongodb.net/?retryWrites=true&w=majority&appName=eternaLib"
#Emre Yörük Hesabı
accounte="mongodb+srv://emreyoruk:VD9qAxtJKPCrkPTq@eternalib.06ijzom.mongodb.net/?retryWrites=true&w=majority&appName=eternaLib"
#Onur Karakaya hesabı
accounto="mongodb+srv://onurkarakaya:rGc9zx2kOzLOtBM5@eternalib.06ijzom.mongodb.net/?retryWrites=true&w=majority&appName=eternaLib"

# process_mongo sınıfını kullanarak MongoDB işlemleri gerçekleştirme
mng = operation_mongo(accounts)

d={"arsa":"apollo"}
r=mng.find_data("deneme","denme","arsa","apollo",filter="_id")
print(r)

# Bağlantıyı kapat
mng.close()
