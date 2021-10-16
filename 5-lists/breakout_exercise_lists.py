# How to create an empty list? 
country_list = []


#----------------------
# How can I add a new element (country) in this list? (Add more than 4, we'll need them in the next steps :) )
country_list.append("Germany")
country_list.append("Brasil")
country_list.append("Russia")
country_list.append("Greece")
country_list.append("Turkey")

print(country_list)



#----------------------
# Get the second country from the country list
second_country = country_list[1]
print(second_country)




#----------------------
# Change the value of the third country, set it to some other country
# print(country_list)
# Change the third country 
country_list[2] = "Italy"
# see what happened
print(country_list)



#----------------------
# When to use insert function? Difference between insert and append? 
country_list.insert(2, "Russia")
print(country_list)



#----------------------
# Remove an element from the list
# print(country_list)
# Remove a country 
# country_list.remove("Italy")
# see what happened


del country_list[3]
print(country_list)





#----------------------
# How to find how many elements are in a list?
print(len(country_list))




#----------------------
# How to get the last element from the list?
print(country_list[len(country_list) - 1])
print(country_list[-1])



#----------------------
# What about the one before last?
print(country_list[-2])





#----------------------
# Slice the list to print the 2nd, 3rd and 4th countries from the list
print(country_list[1:4])



# Find more info about python lists here ->  https://www.w3schools.com/python/python_lists.asp