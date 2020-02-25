#This program demonstrates the parsing capabilities of commmand line arguments in python.
#sys.argv in sys module provides access to command line arguments 
#However, getopt module provides support for parsing the command line arguments via getopt.getopt()
# getopt.getopt(args, options, [long_options])
# args: this is the argument list to be parsed

#Program usage directions:
#command_line_parsing.py -h
#command_line_parsing.py -i test.txt -o
#command_line_parsing.py -i test.txt -o test1.txt


import sys, getopt
def main(argv):
    inputfile = ''
    outputfile = ''
    try: 
        opts,arg = getopt.getopt(argv,"hi:o",["ifile=","ofile="])
    except getopt.GetoptError:
        print('command_line_parsing.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
             print('command_line_parsing.py -i <inputfile> -o <outputfile>')
             sys.exit()
        elif opt in ('-i', '--ifile'):
            inputfile = arg
        elif opt in ('-o','--ofile'):
            outputfile = arg
    print("Input file is ", inputfile)
    print("Output file is ", outputfile)

    if __name__ == "__main__":
        main(sys.argv[1:])