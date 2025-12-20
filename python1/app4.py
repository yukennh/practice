
#sample of updating a list using for loop
doubles = []
for x in range (1,11):
    doubles.append(x * 2)
print(doubles)

#sample of updating a using a for loop with 1 line code
triples = [x * 3 for x in range(1, 11)]
print(triples)

#
fruits = ["apples","mango","peach","orange"]
for fruit in fruits:
    fruit.upper()
print(fruit)

#sample of updating a list of string using format
fruits = ["apples","mango","peach","orange"]
fruits = [fruit.proper() for fruit in fruits]
print(fruits)