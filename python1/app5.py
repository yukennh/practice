
age = int(input("Age: "))

if age >= 18:
    print("You are Registered!")
else:
    print("You are underage!\n")

name = str(input("Name: "))

if name == "":
    print("type your name first: \n")
    name = str(input("Name: "))
else:
    print(f"hello there {name}")