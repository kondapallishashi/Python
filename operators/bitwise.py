#Demonstrates the usage of bitwise operators AND (&), OR (|), XOR (^), Ones Compliment (~), Left Shift (<<), Right Shift (>>)

x = 12
y = 8

#the bin() function can be used to get the binary representation of an integer.
a = bin(x)
b = bin(y)

print("The binary representation of ", x, "is ", a)
print("The binary representation of ", y, "is ", b)

#Performing Binary operations on integer values.
print("The result of binary AND on ", x, "AND", y, "is: ", x & y)
#FIND OUT WHY THIS IS NOT WORKING. IS a and b represented as string.
#print("The result of binary AND on ", a, "AND", b, "is: ", a & b)
print("The result of binary OR on ", x, "OR", y, "is: ", x | y)
print("The result of binary XOR ", x, "XOR", y, "is: ", x ^ y)
print("The result of unary ones compliment on ", x, "is : ", ~x)
print("The result of binary left shift on ", x, "is : ", x<<2)
print("The result of binary right shift on ", x, "is : ", x>>2)

