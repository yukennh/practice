#sample of defining or creating a function
def happy_birthday(name, age): #name and age are arguments here. you can think of it as a variable used within the function
    print(f"happy birthday {name}!") #this is an action in the function where it uses one of the arguments
    print(f"you are {age} years old!")

#sample of invoking / executing a function with the two arguments assigned
happy_birthday("John",40)
happy_birthday("Ryan",13)

#sample of assigning a variable and using that variable as parameter to the argument needed in the function
first_name = str(input("First Name: "))
last_name = str(input("Last Name: "))

def register(firstname, lastname):
    print(f"hi {firstname} {lastname}!")

register(first_name,last_name)

#sample of definining a function with return functionality where the parameter of it's argument are first defined
department = str(input("What is your department? "))
team = str(input("What is your team's name? "))

def group(d,t):
    d = d.capitalize()
    t = t.capitalize()
    return t + " | " + d

orgplace = group(department, team)

print(orgplace)