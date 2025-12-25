import sqlite3
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

un = str(input("user name: "))
print(f"hello {un}!")

action = str(input("What do you want to do?"))

while action not in ['s','t','c']:
    print(f"\n Entry not valid. Below are the following options \n t to register a teacher \n s to create a subject \n c to create a class \n")
    action = str(input("What do you want to do?"))

if action == 's':
    print("proceed with the creation of subject")
elif action == 't':
    print("proceed with registration of teacher")
elif action == 'c':
    print("proceed with the creation of class")

#define action
    #create a subject
    #register a teacher
    #create a class
    