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

#Updating record
up = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Elessar"}})

#Returning updated record
doc = db.students.find_one({"student_id": "1007"})
print("\n -- DISPLAYING STUDENT DOCUMENT FROM fine_one() QUERY --")
print("Student ID:", doc["student_id"], "\nFirst Name:", doc["first_name"], "\nLast Name:", doc["last_name"])
print("\n End of program, press any key to exit...")
_ = getch()
exit()