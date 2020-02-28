#Demonstrates the usage of exceptions in Python.

# The functional code that is likely to cause an exception is enclosed in a try: block.

#Syntax:
# try:
#   Operations that are likely to cause an exception
# except Exception-1 : 
#   If Exception-1 is raised, then execute this suite
# except Exception-2
#   If Exception-2 is raised, then execute this suite
# ......
# ......
# else : 
#   If there is no exception, execute this suite

# A single try statement can have multiple except statements. This is useful as a single statement may throw multiple exceptions
# A generic except clause can be used to handle any/all exceptions
# After the except clauses, an else clause can be used to execute a suite if the try-block does not raise an exception.
# The suite in else clause must be an executable code that does not require try block.


# Program to open a file and handle most common exceptions

try:
    fileObject = open("test.txt","w")
    fileObject.write("This is a sample text.")
except IOError:
    print("Cannot find file or read the file.")
else:
    print("The content is written into the file.")
    fileObject.close()


# The except clause with no exceptions. This catches all the exceptions.
# Not considered as a good programming practice as it does not pin point the exception.

# try:
#   Suite to execute that may cause an exception.
# except:
#   Exception handling suite
# else:
#   If there is no exception, execute this suite.


#The except with multiple clauses.
# 
# try:
#   Suite to execute that may cause an exception.
# except (Exception-1 [,Exception-2] [,Exception-3]...):
#   Exception handling suite
# else:
#   If there is no exception, execute this suite.


# The try-finally statements
# try:
#   suite to test for exceptions
# finally:
#   suite that must execute in case an exception is raised.

# Either the Try-Except or Try-Finally can be used, but not both. Also else cannot be used with finally.
