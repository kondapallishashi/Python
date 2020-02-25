#Demonstrates Assignment operators in python.

x = 15
y = 40
a = 2.5
b = 15.80

# + is the addition operator which adds the operands on either side.
print("Adding two integer values using the + operator: ", x + y)
print("Adding two floating point values using the + operator: ", a + b)
print("Adding one integer value and one floating point value using the + operator: ", x + a)

# - is the subtraction operator which subtracts the RHS operand from LHS operand.
print("Subtracting two integer values using the - operator: ", x - y)
print("Subtracting two floating point values using the - operator: ", a - b)
print("Subtracting one integer value and one floating point value using the - operator: ", x - a)

# * is the multiplication operator which multiplies RHS operand with LHS operand
print("Multiplying two integer values using the * operator: ", x * y)
print("Multiplying two floating point values using the - operator: ", a * b)
print("Multiplying one integer value and one floating point value using the - operator: ", x * a)

# / is the division operator which divides the LHS Operand with RHS Operand
print("Dividing two integer values using the * operator: ", x / y)
print("Dividing two floating point values using the - operator: ", a / b)
print("Dividing one integer value and one floating point value using the - operator: ", x / a)

# % Modulus operator divides the LHS Operand with RHS operand and returns the remainder.
print("The remainder of", x, "/", y, "is", x % y)
print("The remainder of", a, "//", b,"is", a % b)

# ** exponent operator is used to find the exponential value
print("The exponential value of ",x,"**",y,"is: ",x ** y)

# //Floor division operator provides the quotient after truncating the decimal portion.
print("The floor division of ", x, "///", y, "is ", x // y)
