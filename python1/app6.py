#sample of for loop
for x in range (1,11):
    print(x*2)

#sample of for loop for a list
fruits = ["apple","banana","coconut","dalandan"]
for fruit in fruits:
    print(fruit)

#sample of while loop
name = input("Enter your name: ")
while name == "":
    print("Please enter your name.")
    name = input("Enter your name: ") #make sure that you have in a loop a statement to avoid infinite loop
print(f"Hello {name}!")

#sample of while loop
age = int(input("Enter your age: "))
while age < 0:
    print("Please enter a valid age")
    age = int(input("Enter your age: "))
print(f"You are {age} years old {name}")

#sample of while not loop
idea = input("What are you thinking now (q to quit) ?")
while not idea == "q":
    print(f"{name}'s idea is: {idea}")
    idea = input("What are you thinking now (q to quit) ?")
print(f"Got it {name}!")

#sample of while loop with OR
happiness = int(input("From 1 to 10, 10 being the highest, how happy are you today?"))
while happiness < 1 or happiness > 10:
    print("Not a valid answer")
    happiness = int(input("From 1 to 10, 10 being the highest, how happy are you today?"))
print(f"{name}, {age} years old has a lot of ideas. His happiness level is at {happiness}. Have a great day!")


#sample of while not loop with multiple possible condition
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
