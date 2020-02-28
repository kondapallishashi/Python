#Demonstrates how the files can be processed in python.
# The os module provides methods to perform file processing such as renaming, deleting files etc.

import os

#The rename() method renames the files and takes two arguments, current file name and the target file name
os.rename("test.txt", "newtest.txt")

# The file can be removed using the remove("filename") function 
os.remove("newtest.txt")

# To create a new directory use os.mkdir("directoryname")
# The new directory is created in the current directory.
os.mkdir("datafiles")

#To change the current directory use os.chdir("directory Path")
os.chdir("datafiles")
#Check if the / needs to be used with escape characters.
os.chdir("/usr/bin/python/projects/")

# To get the current working directory
os.getcwd()

# To remove a directory use os.rmdir("directory name") or os.rmdir("path")
os.rmdir("datafiles")
os.rmdir("/usr/tmp/test")



