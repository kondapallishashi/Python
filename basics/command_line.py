#This program demonstrates the command line usage in python.
#python sys module provides support for command line arguments via sys.argv.
#sys.argv[0], sys.argv[1].. can be used to access the list of command line arguments, with sys.arg[0] maps to program name
#len(sys.argv) provides the length or the number of arguments that can be used for iterations.

import sys
print("The number of arguments entered by user: ", len(sys.argv)," arguments")
print("Argument list: ", str(sys.argv))
