import certifi
ca = certifi.where()
from pymongo import MongoClient
from msvcrt import getch
url ="mongodb+srv://admin:admin@cluster0.ccrjia9.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient("mongodb+srv://admin:admin@cluster0.ccrjia9.mongodb.net/?retryWrites=true&w=majority", tlsCAfile=ca)
db = client.pytech
names = db.list_collection_names()
print(names)
print("")
print(" End of program, press any key to exit...")
_ = getch()
exit()