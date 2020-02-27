#This program demonstrates the usage of variable arguments.
# A tuple is added to the argument list with a preceding * 
# all additional arguments will go into this tuple and will be processed in the function.

# Syntax of a function with variable arguments
# def functionname(parameters) :
#   "Function doc string"
#   function_suite
#   return [expression]
# 

# Define a simple function that prints the info using the variable length argument list
def printinfo(inputstring, *vartuple) :
    "This prints the variables passed to the function"
    print("The output is: \n")
    print(inputstring, end=' ')

    for var in vartuple : 
        print(var, end=' ')
    return


# Execute the function with multiple parameters
printinfo(10)
printinfo(10,20,30)
printinfo(1,2,3,4,5,6,7,8,10)
