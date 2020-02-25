#Demonstrates various functions that can be used to perform data conversion operations

fruits = ["apples", 45, "grapes", 30]

empId = "150"
#int(x [,base]) converts the integer x in string format to the integer with base if base is specified
#base can be 0 0-26
print("converting the integer in string format to decimal format: ", int(empId))
print("converting the integer in string format to integral formal: ", int(empId,0))


#float(x)

#To create a complex number use complex(real,imag)
print("The complex number created using complex(real,imag) is : ", complex(2,6))

#To convert an object to string
print("Converting a list object to string using str(obj): ", str(fruits))

#To convert an object to an expression string.
repr(x)

#Evaluates a string a returns an object
eval(x)

#converts s to a tuple
tuple(s)

#Converts s to a list
list(s)

#Sets s to a set
set(s)

#creates a dictionary where d is a sequence of key value pairs
dict(d)

#converts s to a frozen set
frozenset(s)

#converts an integer to a character
chr(x)

#Converts an integer to a unicode character
unichr(x)

#Converts a single character to its integer value
ord(x)

#Converts an integer to a hexadecimal string
hex(x)

#Converts an integer to an octal strin
oct(x)
