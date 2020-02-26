#Demonstrates the built in functions for string operations.

string1 = "Hello World"
string2 = "Python Programming"

# [] amd [:] are used to access characters with in a string based on index value or range of values.
print("Print the second, fifth and eigth characters in ", string1, "are: ", string1[1], string1[4], string1[7])
print("print python from string2 : ", string2[0:5])

#Updating strings 
#To Convert Python training to Jython Training.
string2 = "J" + string2[1:]
print(string2)

#To Convert Hello World to Hello Jython, we need to replace from 7th character in string1
string1 = string1[:6] + string2[0:6]
print(string1)

#ESCAPE CHARACTERS
#Covering only the most used escape characters. \n, \r, \s, \t, \v.
#using \n new line character to achieve a multi line print.
print("Welcome\nTo\nThe\nWorld\nOf\nPython\nProgramming\n")
#using \s for spacing between letters.
print("Welcome \sTo\sThe\nWorld\sOf\nPython\sProgramming\n")
#using the \t for tab space
print("Welcome \sTo\sThe\n\tWorld\sOf\n\tPython\sProgramming\n")

#Special String Operators.
#[] [:] & * repeater operators are covered,
#in, not in are also covered.

#Raw Strings.
# r'\n' and R'\n' treats the characters as raw characters and prints them as is.
filepath = 'C:\\downloads'
print(filepath)
filepath = r'C:\\downloads'
print(filepath)


#STRING FORMATTER OPERATOR %
# %c - Character, %s - String, %i - signed decimal integer, %d - signed decimal integer
# %u - unsigned decimal integer, %o octal integer, %x - hexa decimal lower case numbers, 
# %X - hexa-decimal upper case characters, %e - exponential with lowercase e, %E - exponential with uppercase E
# %f - floating point real number



