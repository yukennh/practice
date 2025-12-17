
# dictionary is a collection of set {key: value} pairs that is ordered, changeable and no duplicates
capitals = {"USA": "Washington D.C ",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# to see your dictionary
print(f"{capitals}")

# to see the methods and attributes of the dictionary
print(dir(capitals))
print("---------")
# to get the value in a dictionary using the key
print(capitals.get("USA")) # should return Washington D.C.
print("---------")
print(capitals.get("Philippines")) # should return None
print("---------")
# sample of using if function to check for the key if it exists in the dictionary
country = "USA"
if capitals.get (country):
    print(f"Capital is {capitals.get(country)}.")
else:
    print(f"Capital not found.")
print("---------")
# sample of adding a set pair in dictionary
capitals.update({"Germany": "Berlin"})
print(capitals)
print("---------")
# sample of updating a set pair in dictionary
capitals.update({"USA": "Detroit"})
print(capitals)
print("---------")
# sample of removing a set pair in dictionary
capitals.pop("China")
print(capitals)
print("---------")
# sample of clearing the dictionary
capitals.clear()
print("---------")