#Importing tools and connecting to database
import certifi
ca = certifi.where()
from pymongo import MongoClient
from msvcrt import getch
url ="mongodb+srv://admin:admin@cluster0.ccrjia9.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient("mongodb+srv://admin:admin@cluster0.ccrjia9.mongodb.net/?retryWrites=true&w=majority", tlsCAfile=ca)
db = client.pytech
students = db["students"]

#Displaying full list of current students
docs = db.students.find({})
print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print("Student ID:", doc["student_id"])
    print("First Name:", doc["first_name"])
    print("Last Name:", doc["last_name"],"\n")

#Inserting record
sauron = {
    "student_id": "1010",
    "first_name": "Sauron",
    "last_name": "the Deceiver"
}
sauron_student_id = students.insert_one(sauron).inserted_id
print("Inserted student record", sauron["first_name"], sauron["last_name"], "into the students collection with document_id",  sauron_student_id)

#Returning inserted record
find = db.students.find_one({"student_id": "1010"})
print("\n -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("Student ID:", find["student_id"], "\nFirst Name:", find["first_name"], "\nLast Name:", find["last_name"])

#Deleting the Deceiver
dele = db.students.delete_one({"student_id": "1010"})

#Displaying full list of records
docs = db.students.find({})
print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print("Student ID:", doc["student_id"])
    print("First Name:", doc["first_name"])
    print("Last Name:", doc["last_name"],"\n")

print("\n End of program, press any key to exit...")
_ = getch()
exit()