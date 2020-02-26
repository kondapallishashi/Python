# Demonstrates the functions that can be used with dictionaries in python.

# The dictionaries are defined with key value pairs enclosed within curly {}
# the empty dictionary can be defined using {}
# The key value pairs are separated using colons(:) and the elements are separated using commas (,)
# The key names must be unique and must be immutable such as strings, numbers or tuples.
# The values can be of any data type and need not be unique

#Define a tuple with key names as strings
employee = {'Name': "Sasi", 'Id': 150, 'Designation': "Delivery Manager", 'Salary': 3000, 'Location': "India"}
#Define a dict where keynames could be integers
testDict = {1: 25, 'cost': 233}

# Accessing the elements in the dictionary.
print("Print the name and ID of the employee dictionary: ", employee['Name'], employee['Id'])

#Attempting to access an element with a non existent key will throw a run time error
# Uncomment the below line and test
# print("print the non - existng key name", employee['Experience'])
