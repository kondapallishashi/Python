#Demonstrates the usage of file open and close functionality in Python.

# The files are opened using the open() function.

# open(file_name [,access_mode] [,buffering])

# Access mode determines the mode in which the file is opened. The default is read mode and other modes such as read, write, append etc are there.
# r - read only (default) - file pointer is at the beginning of the file. 
# rb - read only in binary format (default) - file pointer at the begining of the file
# r+ - read and write
# rb+ - read write in binary format
# w - Write only - overwrites the file, if file exists, otherwise it will create a new file
# wb - write only in binary format - overwrites the file, if file exists, otherwise it will create a new file
# w+ - reading & writing - - overwrites the file, if file exists, otherwise it will create a new file
# wb+ - reading and writing in binary format - - overwrites the file, if file exists, otherwise it will create a new file
# a -  append - if the file exists, opens the file in append mode and the file pointer is at the end of the file, otherwise will create a new file.
# ab - append in binary format -  
# a+ - append and reading
# ab+ - append and reading in binary format.


# if the buffering is 0, no buffering takes place, if the buffering is 1, line buffering takes place.
# if buffering is an integer value greater than 1, then buffering takes place with that value.
# if buffering is -ve then the system default buffering is done.

# once the file is opened, a file object is made available and there are several attributes we can use


# Open a file in writing in binary mode and assign it to file object ipfile
ipfile = open("test.txt", "wb")

# file objects file.name - the name of the file
print ("Name of the file: ", ipfile.name)
# file.closed - returns true if file is closed otherwise false
print ("Is the file closed : ", ipfile.closed)
# file.mode - the access mode with which the file is opened
print ("Opening mode : ", ipfile.mode)
#The file objects close() method flushes unwritten information and closes the file after which no information can be written
# Python automatically closes the file, if the file reference is assigned to a different file.
ipfile.close()




