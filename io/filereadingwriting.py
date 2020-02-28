#Demonstrates reading and writing into a file

#Open the file test.txt in write mode
fileobject = open("test.txt", "w")
#Write text into the file using the file objects write() method.
# The text can have binary data as well
# The write method does not include \n at the end of the string.

fileobject.write("Data Scientists depend heavily on statistical analysis and scify, numpy computing that R & Python bring in.\n. So mastering R !! and Python !!! are very important to become great Data Scientists ##")
#Close the file object.
fileobject.close()

# To read the file, open the file in one of the reading modes.
# read() method reads the data from the file.
# read([count]) - count is the number of bytes to be read from the file. If count is missing, the read tries to read as much of the file, may be till the end of the file.

fileread = open("test.txt", "r+")
#read(count) - reads count number of bytes from the file
preview = fileread.read(15)

#The current position is obtained from tell() method. ie the postion from where the next read / write will happen.
position = fileread.tell()
print("The current position in the file is : ", position)

#resetting the position can be done using seek() method.
# seek(offset [,from]) moves the position by offset number of bytes from the 'from' position.
# if from is 0, it is the beginning of the file, if it is 1 it is the current position and if it is 2 it is end of file.

#Setting the file to the beginning of the file.
fileread.seek(0,0)

#moves 10 bytes from the current position
#uncomment below line and test
#fileread.seek(10,1)

#Moves the position by 2 bytes from the end of file
#uncomment below line and test
#fileread.seek(2,2)

# read() with out count will read the file as much as possible, may be till the end if the file size is not too large.
fulltext = fileread.read()

print("The preview of the file is %s" % preview)
print("The full text of the file us %s " % fulltext)

fileread.close()

