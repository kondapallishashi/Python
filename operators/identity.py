#Demonstrates the identity operators is and is not.
#Identity operators check if the two operands are having the same address.

x = 10
y = 10

#Print the values of variables and their ids
print("The value of x is ", x, " and its address id(x) is ", id(x))
print("The value of y is ", y, " and its address id(y) is ", id(y))

#is operator evaluates to true if both operands point to the same object, otherwise it evaluates to false.
if(x is y):
    print("x and y point to the same location")
else: 
    print("x and y do not point to the same location")

#now change the value of one variable.
y=20
print("The value of y is ", y, " and its address id(y) is ", id(y))
#is not operator evaluates to false if both operands point to the same object.
if(x is not y):
    print("x and y do not point to the same location")
else: 
    print("x and y point to the same location")
