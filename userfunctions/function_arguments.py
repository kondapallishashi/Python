# This program demonstrates the usage of arguments / parameters in python.
# covers
# required, default, named parameters.

def area (length, breadth) :
    "This function calculates the area of a qualdrilateral."
    area = length * breadth
    print("The area of a qualdrilateral is", area)
    return

def volume(length, breadth=15, height=10) :
    "This function calculates the volume of the shape"
    vol = length * breadth * height
    print (" The volume of the shape is : ", vol)
    return

# Required Parameters
# Python requires that the correct number of parameters are passed while calling a function.
# These parameters are positional parameters ie the first one is taken as length and the second one is taken as breadth.
#area(30) 

#Here 30 is length and 20 is breadth as parameters in python are positional parameters.
area(30,20)

#However, to pass parameters in a different order, we can use named parameters.
area(length = 20, breadth = 5)
area(breadth = 10, length = 15)

#Check the volume function definition above.
# In the function defintion above, default values have been given to breadth and height.
# if no values are provided, the default values are taken while executing the function.
# since the arguments are positional, if no names are provided, positional mapping is done.

#providing positional parameters. here Length = 10, breadth = 5, height = 2
volume(10,5,2)

#provising only two arguments, here the default value of height is taken.
volume(40,30)
#Default values of breadth and height are taken
volume(35)

#Using named arguments. Here the order is not important and the second argument need not be breadth.
volume (length = 8, breadth = 6, height = 3)
# Default value of breadth is taken.
volume (height=8, length = 12)
#Default value of height is taken.
volume (breadth=18, length = 25)
#Default value of breadth and height are taken.
volume(length = 55)











