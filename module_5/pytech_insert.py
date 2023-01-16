import certifi
ca = certifi.where()
from pymongo import MongoClient
from msvcrt import getch
url ="mongodb+srv://admin:admin@cluster0.ccrjia9.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient("mongodb+srv://admin:admin@cluster0.ccrjia9.mongodb.net/?retryWrites=true&w=majority", tlsCAfile=ca)
db = client.pytech
students = db["students"]
aragorn = {
    "student_id": "1007",
    "first_name": "Aragorn",
    "last_name": "Son of Arathorn"
    }
legolas = {
    "student_id": "1008",
    "first_name": "Legolas",
    "last_name": "from the Woodland Realm"
}
gimli = {
    "student_id": "1009",
    "first_name": "Gimli",
    "last_name": "Son of Gloin"
}
aragorn_student_id = students.insert_one(aragorn).inserted_id
legolas_student_id = students.insert_one(legolas).inserted_id
gimli_student_id = students.insert_one(gimli).inserted_id
print("-- INSERT STATEMENTS --")
print("Inserted student record", aragorn["first_name"], aragorn["last_name"], "into the students collection with document_id",  aragorn_student_id)
print("Inserted student record", legolas["first_name"], legolas["last_name"], "into the students collection with document_id",  legolas_student_id)
print("Inserted student record", gimli["first_name"], gimli["last_name"], "into the students collection with document_id",  gimli_student_id)
print("\n End of program, press any key to exit...")
_ = getch()
exit()