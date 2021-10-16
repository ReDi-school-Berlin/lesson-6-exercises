# What are some differences between dictionaries and lists? 
# dict is not indexable 
# lists are ordered and dictionaries aren't
# dictionaries cannot have duplicate keys




# --------------------
# How to create an empty dictionary
person = {}





# --------------------
# add values for this person, like name, phone, email, address etc in the dictionary
person["name"] = "Harika"
person["phone"] = 125384804
person["address"] = "Berlin"





# --------------------
# Check if the dictionary has a key that doesn't exist (id)
print("id" in person)
print("phone" in person)

# ----------------
# get person's phone. Hint: there are two ways 
# print(person["phone"])
# print(person.get("phone"))

# print(person["id"])
print(person.get("id"))


# ----------------
# Get all the keys of this person dictionary
print(person.keys())



# ----------------
# Get all the values of this person dictionary
print(person.values())



# ----------------
# Change person's address
person["address"] = "Istanbul"
print(person)


# ----------------
# Remove person's phone Hint: two ways to do it (pop/del)
# person.pop("phone")
del person["phone"]
print(person)
person.clear()
print(person)








# Find more info about python dictionaries here -> https://www.w3schools.com/python/python_dictionaries.asp