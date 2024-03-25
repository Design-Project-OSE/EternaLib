import pymongo 

myclient= pymongo.MongoClient("mongodb+srv://sinanuygun:BnKJOKx7OTvSWLfD@eternalib.06ijzom.mongodb.net/")

mydb=myclient["mgb_data"]

print(myclient.list_database_names())