#Demonstrates the finally clause in the exceptions.

try:
 fh = open("test.txt", "w")
 fh.write("This is my test file for exception handling!!")
finally:
 print ("Error: can\'t find file or read data")
 fh.close()