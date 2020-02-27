#Demonstrates the structure of the function

# In python the functions start with def keyword followed by the function name followed by parenthesis, followed by colon (:)
# The input parameters are defined or listed in the parenthesis.
# The function code block can start with documentation string
# The code block is indented 
# The return statement exits the function returns the parameter back to the function calling statement.
# if there is no return parameter, empty return statement can be used or return none can be used.

# Function syntax

#   def functionname (paremeters) :
#       "function_docstring"
#       function_suite
#       return [expression]
# 

# Define a function that takes in a string as input parameter and prints the string value.
def printStatement (inputString) :
    "This method prints a string that is passed via inputString"
    print(inputString)
    return 

#Calling the printStatement function
printStatement("Print this first statement")

# Calling the printStatement function a second time.
printStatement("Print this second statement")

def sum( arg1, arg2 ):
 # Add both the parameters and return them."
 total = arg1 + arg2
 print ("Inside the function : ", total)
 return total
# Now you can call sum function
total = sum( 10, 20 )
print ("Outside the function : ", total )
