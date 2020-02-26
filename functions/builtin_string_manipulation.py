#Demonstrates the built in methods for String Manipulation.
import base64 
#import maketrans
#this module is imported to support base64 operations in encode decode,


string1 = "this is in lower case"

# Capitalize() - Capitalizes the first character.
print("Capitalize the first character in %s and display \n: %s" % (string1, string1.capitalize()))

# center(width [,fillchar]) - Centers the string to the length of width and fills the spaces with the fillchar.
#Default is space.
print("Center the string %s and fill with *: \n %s" % (string1,string1.center(40,'*')))

#count(substring [,start] [,end]) - returns the count of occurances of sub string starting from index start and ending with index end.
#by default start is 0 and end is last index or len(string)

#consider the string1 = this is in lower case.
#leaving out start and end to default values.
print("The number of occurances of i in %s is %d" % (string1, string1.count('i')))
# counting the number of o's in string1. 
# Since we know its not in the last part of sentence and first part of sentence, we can define limits.
print("The number of occurances of o in %s is %d" % (string1, string1.count('o', 10, 18)))
#Counting the number of e's in the string1.
print("The number of occurances of e in %s is %d" % (string1, string1.count('e', 10)))

#endswith(suffix [,starts] [,ends]) 
#returns True or False depending on whether the sentence ends with the given suffix. Suffix can be a single character or a substring
# start and end specify the indexes from which the matching is done.
#this is in lower case
suffix1 = "case"
suffix2 = 'low'

print("The sentence: %s ends with %s : %s" % (string1, suffix1, string1.endswith(suffix1)) )
print("The sentence: %s ends with %s : %s" % (string1, suffix1, string1.endswith(suffix1,8)) )
print("The sentence: %s ends with %s : %s" % (string1, suffix2, string1.endswith(suffix2,8,14)) )
print("The sentence: %s ends with %s : %s" % (string1, suffix2, string1.endswith(suffix2,8,15)) )

#expandtab(tabsize=8) expands the tab with the given tabsize spaces. Default tabsize is 8.
print("The expandtab() expands the string with spaces: ", "sentence\twith\ttabs".expandtabs())

# find(substring, beg, end) returns index if found or -1 if not found. beg index is by default 0 and end is len(string)
substr = 's in'
print("The substring: %s :occurs in %s at %d " % (substr,string1, string1.find(substr)))
print("The substring: %s :occurs in %s at %d " % (suffix1,string1, string1.find(substr,10,18)))
print("The substring: %s :occurs in %s at %d " % (suffix1,string1, string1.find(substr,20)))
print("The substring: %s :occurs in %s at %d " % (suffix2,string1, string1.find(substr,5,18)))

# index(substr [,beg] [,end]) returns index if found or throws a runtime exception.
print("The index of substring - %s in sentence: %s is %d" %(suffix1, string1, string1.index(suffix1)))
print (string1.index(substr, 0,19))
print (string1.index(suffix2,0,19))

# isalnum()
trueTestString = 'textand2345'
falseTestString = 'total text'
print("The sentence - %s is alphanumeric: %s" % (trueTestString, trueTestString.isalnum()))
print("The sentence - %s is alphanumeric: %s" % (falseTestString, falseTestString.isalnum()))

# isalpha()
trueTestString = 'totaltext'
falseTestString = 'total text!'
print("The sentence - %s is alphabetic: %s" % (trueTestString, trueTestString.isalpha()))
print("The sentence - %s is alphabetic: %s" % (falseTestString, falseTestString.isalpha()))

# isdigit()
trueTestString = '234567'
falseTestString = 'This are some numbers 34'
print("The sentence - %s is digits: %s" % (trueTestString, trueTestString.isdigit()))
print("The sentence - %s is digits: %s" % (falseTestString, falseTestString.isdigit()))

# islower()
# isupper()
# isnumeric()
trueTestString = '87654'
falseTestString = 'house number 68'
# isspace()
trueTestString = '         '
falseTestString = 'Sentence has spaces'
# istitle()
trueTestString = 'This Is A Sentence With Title Case'
falseTestString = 'This is not a sentence with title case'

#join()
sentence = '-'
sequence = ("To", "hell", "with", "that")
print(sentence.join(sequence))

#len(string)
print("The length of the string - %s is %d" % (string1, len(string1)))

#ljust(width [,fillchar]) returns a string with the width provided and padding done by the fillchar.
# default padding character is space.
print("The sentence - %s - left justified to 30 width is %s" % (string1, string1.ljust(30)))
print("The sentence - %s - left justified to 30 width with * as fillchar is %s" % (string1, string1.ljust(30,'*')))

# lstrip()

str = " this is string example....wow!!!"
print (str.lstrip())
str = "*****this is string example....wow!!!*****"
print (str.lstrip('*'))


# maketrans(intab, outtab) makes a table mapping elements in intab with corresponding elements in outtab.
# intab string having actual characters
# outtab string having corresponding mapping characters

intab = 'aeiou'
outtab = '12345'
trantab = string1.maketrans(intab,outtab)
print(trantab)

# translate() translate the string using the trantab table where the actual characters are replaced with mapped characters.

print("The translated sentence of - %s - using the translate table %s is : %s" % (string1, trantab, string1.translate(trantab)))

#max() returns the maximum occuring alphabet in the sentence.
print("The maximum occuring letter in the sentence - %s - is %s " % (string1, max(string1)) )

#min()
print("The minimum occuring letter in the sentence - %s - is %s " % (string1, min(string1)) )

#replace( str [,max])
str = "this is string example....wow!!! this is really string"
print (str.replace("is", "was"))
print (str.replace("is", "was", 3))

#str.rfind(str, beg=0 end=len(string))
str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rfind(str2))
print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 0))
print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 0))

# str.rindex(str, beg=0 end=len(string))
str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rindex(str2))
print (str1.rindex(str2,10))

#str.rjust(width[, fillchar])

str = "this is string example....wow!!!"
print (str.rjust(50, '*'))

# str.rstrip([chars])
str = " this is string example....wow!!! "
print (str.rstrip())
str = "*****this is string example....wow!!!*****"
print (str.rstrip('*'))

#str.split(str="", num=string.count(str)).


str = "this is string example....wow!!!"
print (str.split( ))
print (str.split('i',1))
print (str.split('w'))

#str.splitlines( num=string.count('\n'))
str = "this is \nstring example....\nwow!!!"
print (str.splitlines( ))

# str.startswith(str, beg=0,end=len(string));
str = "this is string example....wow!!!"
print (str.startswith( 'this' ))
print (str.startswith( 'string', 8 ))
print (str.startswith( 'this', 2, 4 ))

#str.strip([chars]);
str = "*****this is string example....wow!!!*****"
print (str.strip( '*' ))

#str.swapcase();
str = "this is string example....wow!!!"
print (str.swapcase())
str = "This Is String Example....WOW!!!"
print (str.swapcase())

#str.title();
str = "this is string example....wow!!!"
print (str.title())

# str.translate(table[, deletechars]);

#from string import maketrans # Required to call maketrans function.
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
str = "this is string example....wow!!!"
print (str.translate(trantab))

#from string import maketrans # Required to call maketrans function.
intab = "aeiouxm"
outtab = "1234512"
trantab = str.maketrans(intab, outtab)
str = "this is string example....wow!!!"
print (str.translate(trantab))

# str.upper()
str = "this is string example....wow!!!"
print ("str.upper : ",str.upper())

# str.zfill(width)
str = "this is string example....wow!!!"
print ("str.zfill : ",str.zfill(40))
print ("str.zfill : ",str.zfill(50))

# str.isdecimal()
str = "this2016"
print (str.isdecimal())
str = "23443434"
print (str.isdecimal())






#encode() and decode()
#encode(encoding='UTF-8', errors='strict') method encodes the string to using the default current encoding scheme.
# errors ='strict' can be passed to different error handling mechanisms such as ignore, replace, xmlcharrefreplace, backslashreplace or any other name registered via codecs.register_error().
# strict raises unicode errors.
# to use base64.b64encode import base64 module.
encodedString1 = string1.encode('base64','strict')
print('Encoded string1 %s in base 64 is %s' % (string1,encodedString1))

decodedString1 = encodedString1.decode('base64', 'strict')
print('decoded string of %s is %s' %(encodedString1, decodedString1))

encodedString2 = base64.b64encode(string1.encode(encoding='UTF-8',errors='strict'))
print("Encoded string of %s is: %s" %(string1,encodedString2))

#CHECK THE ABOVE BLOCK OF CODE RETURNING base64 is not a text encoding. use codecs.encode() 






