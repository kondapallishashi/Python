# Demonstrates the functions that can be used with dictionaries in python.

# The dictionaries are defined with key value pairs enclosed within curly {}
# the empty dictionary can be defined using {}
# The key value pairs are separated using colons(:) and the elements are separated using commas (,)
# The key names must be unique and must be immutable such as strings, numbers or tuples.
# When duplicate keys are used, the last provided key is taken.
# The values can be of any data type such as python objects, user defined objects or standard objects and need not be unique

#Define a tuple with key names as strings
employee = {'Name': "Sasi", 'Id': 150, 'Designation': "Delivery Manager", 'Salary': 3000, 'Location': "India"}
#Define a dict where keynames could be integers
testDict = {1: 25, 'cost': 233}
#Define a dictionary with list as key. Throws a runtime error list objects are unhashable
#Uncomment the below line and test
#listKey = {["Name"]: "Sasi", "ID": 150}



#An empty Dictionary can be defined with no elements. The elements can be added later.
noElements = {}

#To define a dictionary with single element, the element must be followed by a comma.
singleElement = {59,}

# dictionary with duplicate keys. Here Name: Sasidhar & ID:152 are considered.
dupeKeys = {'Name': "Sasi", 'ID': 150, 'Name': "Sasidhar", 'ID': 152}
print("Print the name and ID of the dupeKeys dictionary: ", dupeKeys)


# Accessing the elements in the dictionary.
print("Print the name and ID of the employee dictionary: ", employee['Name'], employee['Id'])

#Attempting to access an element with a non existent key will throw a run time error
# Uncomment the below line and test
# print("print the non - existng key name", employee['Experience'])

#To Update the existing elements, access the value by key and assign new value.
employee['Name'] = "Sasidhar"
employee['Id'] = 152
print("Print the updated name and ID of the employee dictionary: ", employee['Name'], employee['Id'])

#Adding new key-value pairs to the dictionary.
print("The original elements in testDict dictionary: ", testDict)
testDict['quantity'] = 83
testDict['product'] = "Books"
print("The updated elements in testDict dictionary: ", testDict)

#Deleting elements in the dictionary.
#To delete specific elements in the dictionary, use del in conjunction with keyname.

del testDict['quantity']
print("The updated elements in testDict dictionary: ", testDict)

# Removes all the elements in the dictionary, but the dictionary is available.
# The length of the dictionary becomes 0. This method does not return any value.
testDict.clear()

#Deletes the entire dictionary and the reference to it as well.
del testDict

#Common functions used with dictionaries.

#cmp(dict1, dict2) - Deprecated in python 3

# len(dict)
print("The number of elements in dictionary employee: len(employee): ", len(employee))
print("The number of elements in dictionary dupeKeys: len(dupeKeys): ", len(dupeKeys))

# str(dict)
print("The string representation of employee dictionary str(employee): %s" % str(employee))

# type(variable)
print("The type of employee dictionary type(employee): %s" % type(employee))

# Methods that can be used with dictionaries.

# dict.clear()

# dict.copy()
#This method returns a shallow copy of the dictionary.
employeeCopy = employee.copy()
print("The copy of employee dictionary: %s" % str(employeeCopy))


# dict.fromkeys()
# This method returns a dictionary with keys from the sequence and the values if supplied are assigned.
seq = ('Name', 'ID', 'Designation')
# Since no value is provided, None will be present in place of all values.
empKeys = employee.fromkeys(seq)
print("The dictionary obtained by using fromkeys() is: %s" % str(empKeys))

#Provide some default value 5
empKeys1 = employee.fromkeys(seq,10)
print("The dictionary obtained by using fromkeys() is: %s" % str(empKeys1))

# dict.get(key, default=none)
# This method returns the value of the key provided. If the key is not present, the default value None is returned.
# We can provide the default value to be returned using default='NA'

print("The value of Key Name in employee dictionary: ", employee.get('Name'))
print("The value of non existent Key Age in employee dictionary: ", employee.get('Age'))
print("The value of non existent Key Age in employee dictionary: ", employee.get('Age', 'NA'))

# dict.has_key(key)


# dict.items()
# This method returns the dictionary's key value pairs in a tuple.
print("The items of the dictionary employee in tuple pairs employee.items(): %s " % employee.items())

# dict.keys()
# This method returns all the keys in the dictionary in a list..
print("The keys in the dictionary employee: %s" % employee.keys())

# dict.setdefault(key, default=none)
# This method sets the default value of the key and if the key is not listed, then the default value is returned.
# Setting the default value to an existing key
employee.setdefault('ID',None)
# setting the default value to a key thats not existing.
employee.setdefault('Age', None)
# Observer the Age value in the print statement.
print(" The dictionary employee after default value set for ID and Age %s" % str(employee))

# dict.update(dict2)
# This method adds dictionary dict2 key value pairs to the dict dictionary.
address = {"street": "Shilpa Avenue Colony", "city": "Hyderabad"}
employee.update(address)
print("The updated employee dictionary with address : %s" % str(employee))

# dict.values()
# This method returns a list with all values in the dictionary.
print("The values of the employee dictionary: ", list(employee.values()))




