
name = "ken"
profession = "dev"

#sample of string.format
print("I am {}. I am a {}".format(name,profession))
print(f"--------\n")

#sample of string.format that uses index as positional argument
print("I am {0}. I am a {1}.".format(name, profession))
print("I am {1}. I am a {0}.".format(name, profession))
print(f"--------\n")

#sample of string.format that uses keyword argument
print("He is {person1} and I am {person2}".format(person1 = "john", person2 = "ryan"))
print("He is {person2} and I am {person1}".format(person1 = "john", person2 = "ryan"))
print(f"--------\n")

#sample of string.format wherein the variables and the text are defined and the string formatting was just done at the end
animal = "cat"
food = "fish"
text = "the {} is eating the {}"
print(text.format(animal, food))
print("--------\n")

#sample of string manipulation by adding a padding to the right of the variable.
level = "2"
company = "ABC"
print("I am a level {:10}. I work at {}".format(level, company))
#sample aligning to left
print("I am a level {:<10}. I work at {}".format(level, company))
#sample aligning to right
print("I am a level {:>10}. I work at {}".format(level, company))
#sample aligning to center
print("I am a level {:^10}. I work at {}".format(level, company))

#sample of formatting to get only the specific number of decimal
number = 3.14159
print("The number pi is {:.2f}".format(number))
print("--------\n")

#sample of formatting to get only the specific number of decimal
number1 = 1000

print("The number is {:,}".format(number1))
print("The number is {:b}".format(number1))
print("The number is {:o}".format(number1))
print("The number is {:X}".format(number1))
print("The number is {:E}".format(number1))