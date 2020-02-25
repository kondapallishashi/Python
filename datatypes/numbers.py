#Demonstrates the numeric data types in python
#Python supports 5 data types: Numeric, String, List, Tuple, Dictionary

#Numeric Data Types. 
#Numeric objects are created when an integer, floating point or complex integer value is assigned to the variable

#Signed Integer Numeric Data Types
#All integer numbers are represented as signed long numbers in python 3. There is no separate long type
length = 5
breadth = 10
bignumber=1000000000000000 #This number gets appended with L when printed.
discount = -12

#numbers can be preceded with 0 with no effect
rate = 080

#Integer numbers can also be represented in Octal format
octal_rate = 0x260
octal_range = -0x26

#FLOATING POINT NUMBERS
pi = 3.14
torque = -2.83

#floating point numbers can be represented in exponential format as well
#e can be uppercase E as well
exp1 = 4+e3 
exp2 = -3+e5
exp3 = 2+E6
exp4 = 2E6
exp5 = 2-e3


#the digits after decimal point are optional if they are zero
no_decimal = 09.

#Complex Numbers
comp1 = 3.14j
comp2 = 34+4J
comp3 = 2e+5j

#A reference to a numeric object can be deleted using del keyword
#del var1
#del var1, var2,...

del exp2, comp2, length, height


