from mongo_process import operation_mongo
from flask import Flask, jsonify

#Sinan Uyğun hesabı
accounts="mongodb+srv://sinanuygun:BnKJOKx7OTvSWLfD@eternalib.06ijzom.mongodb.net/?retryWrites=true&w=majority&appName=eternaLib"
#Emre Yörük Hesabı
accounte="mongodb+srv://emreyoruk:VD9qAxtJKPCrkPTq@eternalib.06ijzom.mongodb.net/?retryWrites=true&w=majority&appName=eternaLib"
#Onur Karakaya hesabı
accounto="mongodb+srv://onurkarakaya:rGc9zx2kOzLOtBM5@eternalib.06ijzom.mongodb.net/?r"
mng = operation_mongo(accounts)

collec_movie=mng.get_collection("mgb_data","movie")
app = Flask(__name__)

@app.route('/movies', methods=['GET'])
def get_data():
    data = collec_movie
    return jsonify(data)


if __name__ == '__main__':
    app.run()

mng.close()