#sample of string variable
first_name = "kenneth" 
last_name = "yu" 

#sample of integer variable
age = 35 
distance = 10

#sample of float variable
speed = 7.2

#sample boolean
status = False 
strava = True

print(f"{first_name} {last_name}, age {age}, will be running for {distance} km with speed of {speed}km/h. Is he an active runner? {status}. Is he on strava? {strava}.")

# there are three types of collection
    # list
    # Set
    # Tuple
#sample of collections with list type. list are enclosed by []
fruitsalad =["apple","grapes","peach","pear"]

#sample print
print(f"My fruit salad has {fruitsalad}")

#sample of calling a specific value within a list by referring to index number, always starting with 0. Value within an collection is called an element
print(f"My favorite fruit is {fruitsalad[3]}")

#sample of calling a specific element in a list by stating the index range (option 1)
print(f"i love {fruitsalad[0:2]}fruits")

#sample of calling a specific element in a list by stating the index range (option 2)
print(f"i love {fruitsalad[:2]}fruits")

#sample of calling a specific element in a list by stating the index range (option 3)
print(f"i love {fruitsalad[::2]}fruits")

#sample of calling a specific element in a list by stating the index range (option 4)
print(f"i love {fruitsalad[::-1]}fruits")

# to check all the attributes & methods that can be done in the collection
print(dir(fruitsalad))

# to check the definition of methods in the collection
#print(help(fruitsalad))

# to check the number of elements in a collection
print(len(fruitsalad))

# to check if an element is in a collection
print("apple" in fruitsalad) # should return True
print("chico" in fruitsalad) # should return False

# to change an element based by using index
fruitsalad[0] = "pineapple"

# sample of loop to make action to each element in the collection
for fruit in fruitsalad:
    print(f"{fruit}")

print("------")

# sample of using a method or attribute. sample is adding an element to the list and checking if added by doing print
fruitsalad.append("dragon fruit")

for fruit in fruitsalad:
    print(f"{fruit}")