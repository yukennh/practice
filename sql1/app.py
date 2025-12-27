import sqlite3

un = str(input("user name: "))
print(f"hello {un}!")

action = str(input("What do you want to do?"))

while action not in ['s','t','c','q']:
    print(f"\n Entry not valid. Below are the following options \n t to register a teacher \n s to create a subject \n c to create a class \n")
    action = str(input("What do you want to do?"))

if action == 's':
    print("Provide subject details.")
    subj_name = str(input("Subject Name: "))
    subj_code = str(input("Subject Code: "))
    subj_credits = float(input("Subject Credits: "))
    
    def create_s(name, code ,credits):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO subjects (subject_name, subject_code, credits) VALUES(?,?,?)",(name, code, credits))
        conn.commit()
        print("Your subject is created!")
        conn.close()
    create_s(subj_name, subj_code, subj_credits)

elif action == 't':
    print("Provide teacher's details.")
    t_fname = str(input("First Name: "))
    t_lname = str(input("Last Name: "))
    t_email = str(input("Email Address: "))
    t_department = str(input("Department: "))

    def create_t(f_name, l_name, email, department):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO teachers (first_name,last_name,email,department) VALUES(?,?,?,?)",(f_name, l_name, email, department))
        conn.commit()
        print("Your subject is created!")
        conn.close()
    create_t(t_fname, t_lname, t_email, t_department)

elif action == 'c':
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    print("Provide class details.\n")
    
    cursor.execute("SELECT subject_id, subject_name FROM subjects")
    s_entries = cursor.fetchall()
    for s_entry in s_entries:
        print(s_entry)
    c_subject = int(input("Subject ID (see IDs above): "))
    
    cursor.execute("SELECT teacher_id, first_name || ' ' || last_name, department FROM teachers")
    t_entries = cursor.fetchall()
    for t_entry in t_entries:
        print(t_entry)
    c_teacher = int(input("Professor ID (see IDs above): ")) 

    c_semester = str(input("\nSemester: "))
    c_schedule = str(input("\nSchedule: "))
    c_room = str(input("\n Room: "))
    
    def create_c(subject, teacher, semester, schedule, room):
        cursor.execute("INSERT INTO classes (subject_id, teacher_id, semester, schedule, room) VALUES (?,?,?,?,?)",(subject, teacher, semester, schedule, room))
        conn.commit()
        print("Class created successfully!")
        conn.close()
    create_c(c_subject, c_teacher, c_semester, c_schedule, c_room)

elif action == 'q':
    print(f"goodbye {un}!")


    
    