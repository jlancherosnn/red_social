from pymongo import MongoClient
import certifi

MONGO = 'mongodb://jlancherosn:jlancherosn@ac-g6o0789-shard-00-00.qzbinqn.mongodb.net:27017,ac-g6o0789-shard-00-01.qzbinqn.mongodb.net:27017,ac-g6o0789-shard-00-02.qzbinqn.mongodb.net:27017/?ssl=true&replicaSet=atlas-fn1vjs-shard-0&authSource=admin&retryWrites=true&w=majority'
cetificado = certifi.where()

def Conexion():
    try:
        print("CONEXION EXITOSA")
        client =MongoClient(MONGO,tlsCAFile=cetificado)
        bd= client["bd_publicaciones"]
    except ConnectionError:
        print("RECHAZO CONEXION")
    return bd
