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
    print("Provide subject details.")
    subj_name = str(input("Subject Name: "))
    subj_code = str(input("Subject Code: "))
    subj_credits = float(input("Subject Credits: "))
    
    subj_confirm = bool(input(f"Confirm Changes\nSubject Name:{subj_name} \nSubject Code:{subj_name} \nSubject Credits:{subj_credits} \n(y/n)?"))
        
    print(f"INSERT INTO subjects (subject_name, subject_code, credits) VALUES({subj_name},{subj_code},{subj_credits})")

elif action == 't':
    print("Provide teacher's details.")
    t_fname = str(input("First Name: "))
    t_lname = str(input("Last Name: "))
    t_email = str(input("Email Address: "))
    t_department = str(input("Department: "))
    print(f"INSERT INTO teachers (first_name,last_name,email,department) VALUES({t_fname},{t_lname},{t_email},{t_department})")
elif action == 'c':
    print("Provide class details.")
    print("Subject ID: ")
    print("Teacher ID: ")
    print("Semester: ")
    print("Schedule: ")
    print("Room: ")
    

#define action
    #create a subject
    #register a teacher
    #create a class
    