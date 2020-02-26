#Demonstrates built in numerical functions.
#refer to the numbers.py in datatypes for basic information on numerical types.

import math #This module is imported to support the math functions listed below.


s = "10" #Note that input() function returns the entered values in string format.
x = 10

#Basic conversion functions.
#use int(x) function to convert the integer in string format to integer.
print("The integer value in string s", s, "can be converted using int(s): ", int(s))
#CHECK IF LONG CONVERSION IS DEPRECATED AS IN PYTHON 3 ALL INTEGER VALUES ARE TREATED AS LONG VALUES.
#print("To convert integer to long using long(x): ", long(x))
print("To convert integer to float use float(x): ", float(x))
print("To convert integer to complex use complex(x)", complex(x)) #this converts the integer to real part of complex and the imaginary part will be zero.

#use complex(real,imag) function to create a complex number.
comp_num = complex(int(s),x)
print("Complex number is: ", comp_num)

#BASIC MATHEMATICAL FUNCTIONS
#Import math module for some of these functions.

#abs(x) function returns the absolute value of x, ie the positive distance of x from zero.
print("The absolute value of -45 is: ", abs(-45)) #prints 45
print("The absolute value of 3.14 is: ", abs(3.14)) #prints 3.14

#ceil(x) returns the smallest integer that is less than x.
print("The ceil value of -10.47 is : ", math.ceil(-10.47)) #
print("The ceil value of 10.47 is : ", math.ceil(10.47)) # prints 11
print("The ceil value of 10.47 is : ", math.ceil(10.67)) # prints 11

#exp(x) function returns the exponential value of x ie e power x.
print("The exponential value of -10.47 is: ", math.exp(-10.47))
print("The exponential value of 10.47 is: ", math.exp(10.47))

#fabs(x) provides the absolute value of x and is similar to abs(x).
#The difference is fabs() is defined in math module, where as abs is a built-in function.
#fabs() works on float and integer type of numericals where as abs() works on complex numbers as well.
print("The f absolute value of -45 is: ", math.fabs(-45)) #prints 45
print("The f absolute value of 3.14 is: ", math.fabs(3.14)) #prints 3.14

#floor(x) returns the floor value of x, ie the largest integer that is less than x.
print("The floor value of -10.47 is : ", math.floor(-10.47)) #
print("The floor value of 10.47 is : ", math.floor(10.47)) # prints 10
print("The floor value of 10.87 is : ", math.floor(10.87)) # prints 10

#log(x) returns the natural logarithm of x where x is greater than 0
#The below statement throws a runtime error as x is a negative value.
#print("The log of -10.47 is: ",math.log(-10.47))
print("The log of 10.47 is: ",math.log(10.47))

# max(x1, x2, x3, ...xn) returns the maximum number of its arguments.
print("The maximum value of the collection max(0, 100, 300, 60, 12) is: ", max(0, 100, 300, 60, 12))
print("The maximum value of the collection max(0, -100, -300, -60, -12) is: ", max(0, -100, -300, -60, -12))

# max(x1, x2, x3, ...xn) returns the maximum number of its arguments.
print("The maximum value of the collection max(0, 100, 300, 60, 12) is: ", max(0, 100, 300, 60, 12))
print("The maximum value of the collection max(0, -100, -300, -60, -12) is: ", max(0, -100, -300, -60, -12))

# min(x1, x2, x3, ...xn) returns the minimum number of its arguments.
print("The minimum value of the collection max(0, 100, 300, 60, 12) is: ", min(0, 100, 300, 60, 12))
print("The minimum value of the collection max(0, -100, -300, -60, -12) is: ", min(0, -100, -300, -60, -12))

# modf(x) returns the gractional and integer parts of x in a two item tuple. The integer part is returned as a float and both the values carry the sign of the original number.
#log(x) returns the natural logarithm of x where x is greater than 0
print("The modf() value of -10.47 is: ",math.modf(-10.47)) 
print("The modf() value of 10.47 is: ",math.modf(10.47))

# pow(x,y) returns the value of x power y.
print("The value of pow(10,2) is: ", pow(10,2))
print("The value of pow(10,-2) is: ", pow(10,-2))

# round(x [,size]) returns the rounded value after limiting the number of decimal digits to size mentioned. Default is 0.
print("The rounded value of round(3.14582) :", round(3.14582)) # 3 as default digits are 0
print("The rounded value of round(3.14582,2) :", round(3.14582,2)) # 3.15 as portion after 4 is rounded off to higher value
print("The rounded value of round(3.14082,2) :", round(3.14082,2)) # 3.14 as portion after 4 is rounded off to lower value
print("The rounded value of round(-3.14582,2) :", round(-3.14082,2))

# sqrt(x) returns the square root of x where x > 0
print("The square root of 34 is : ", math.sqrt(34))
#The below line throws a runtime error as x is a negative value.
#print("The square root of -34 is : ", math.sqrt(-34))


