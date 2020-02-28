#Demonstrates the file methods that can be used on files.



fileobject = open("programming.txt", "r+")

# file.name()
print("The file name is : \n",fileobject.name)

#file.fileno() - returns an integer file descriptor that the underlying implementation uses for IO
filenumber = fileobject.fileno()
print("The file descriptor (fileno) is: \n", filenumber)

# file.isatty() - returns true if the file is connected to a tty like device otherwise returns false
print("Is this file connected to a tty (like) device: \n", fileobject.isatty())

# next(file) - returns the next line from the file everytime it is called.
# Depricated in python 3. Check the alternatives.
#for index in range(10):
#    line = fileobject.__next__()
#    print("The line# %d is: %s " % (index,line) )

# file.read([size]) - Reads the size of bytes from the file. if size is not mentioned, will attempt to read the file.
#reads 10 bytes from the file. Please note that the position will be some where middle of the file from previous function.
position = fileobject.tell()
line = fileobject.read(10)
print("Reading 10 bytes from the position %d is: %s" % (position, line))

# reading with out size. Note the position will not be the beginning of the file.
line = fileobject.read()
print("The remaining text in the file is: \n", line)

#After printing, setting the file position back to the 15 bytes from the beginning of the file.
fileobject.seek(15,0)

#file.readline([size]) - reads one entile line from the file. A trailing newline character is kept in the string
line = fileobject.readline(3)
print("The readline with size 3 is: \n", line)

line = fileobject.readline()
print("The readline with out any size is: \n", line)

# file.readlines([sizehint]) - Reads until EOF using readline() and return a list containing the lines. If the
#  optional sizehint argument is present, instead of reading up to EOF, whole lines
#  totalling approximately sizehint bytes (possibly after rounding up to an internal
#  buffer size) are read.

line = fileobject.readlines(2)
print("The readlines with size 2 is: \n",line)

line = fileobject.readlines()
print("The readlines with no size is: \n", line)

#file.flush() - 


#file.seek(offset [,from])
#Setting the position to beginning of the file.
fileobject.seek(0,0)


# file.tell() - current position in the file.

#file.truncate([size]) - truncates the file size. if size is given, it will truncate to almost the size provided
fileobject.truncate()
line = fileobject.readlines()
print("The content after truncate using readlines is: ", line)

fileobject.close()

fileobject = open("programming.txt","w+")
#Setting the file position to end of the file.
fileobject.seek(0,2)

#file.write(str)
fileobject.write("bThis is the new text being written using write method.!!")

#file.writelines(sequence) - The sequence can be any iterable object producing strings, like lists etc.
seq = ["This is additional lines 1 \n", "More additional lines\n", "Even more additional lines\n"]
fileobject.writelines(seq)

fileobject.seek(0,0)
line = fileobject.read()
print("The text read using read() is : \n", line)

#file.close()
# file.close() can be called more than once. Once closed any opertion that requires file to be open will cause Value Error.
# if file reference changes, the file will be automatically closed by python.
# after the file is closed no read/write operations can be performed.
fileobject.close
