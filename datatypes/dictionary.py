#Demonstrates the usage of dictionary data type in python.
#dictionaries are defined with elements of any python types with in {}, mostly in key-value pairs
#dictionary data types consist of key value pairs where keys are almost any python data types but are mostly numbers or strings
#The values can be any python data types.
#The elements in the dictionary are unordered

#Define an empty dictionary
student = {}
#add to a dictionary where the key type is a string.
student['mission'] = {"The mission is to learn python"}
#add to a dictionary where the key type is a number.
student[150] = "Student ID"

#Define a dictionary where there are multiple key-value pairs
employee = {"Id": 150, "Name": "Sasidhar Kondapalli", "dept": "Delivery", "Experience": 17.6, "Salary": 30000}

#Printing the dictionaries
print("The dictionary with string type key is ", student['mission'])
print("The dictionary with numerical type key is ", student[150])
print("The full employee dictionary is ", employee)
print("To print the keys of dictionary employee, use employee.keys(): ", employee.keys())
print("To print the values of dictionary employee, use employee.values(): ", employee.values())

