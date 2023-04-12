first_name = "Katie"
surname = "Sheridan"

#simple print first and last name
print(first_name + surname)

#print name + string
print(f"My first name is {first_name}. My family name is {surname}")

#combine string and integer
my_int = 34
sentence = "My age is: "
print(sentence + str(my_int))

#create dictionary
user = {"first_name":"Katie"}
print(user)
{'first_name': 'Katie'}

#read the value of the key
user = {"first_name":"Katie"}
print(user["first_name"])

#Add a key value to the dictionary
user["family_name"] = "Sheridan"
print(user)
{'first_name': 'Katie', 'family_name': 'Sheridan'}

#Modify a vlue
user["family_name"] = "Lovelace"
print(user)
{'first_name': 'Ada', 'family_name': 'Lovelace'}

#Delete a Key Value Pair
del user["family_name"]
print(user)
{'first_name': 'Ada'}

#create a list
pokemon = ["squirtle", "bulbasaur", "Charmander"]

len(pokemon) 