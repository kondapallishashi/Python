#Demonstrates iterator object in python
#iterator is an object that supports iterating through all elements of a collection, regardless of its specific implementation.
#Iterator object implements two methods iter() and next().
#String, list or tuble objects can be used to create an iterator.

import sys
#importing sys module to support sys.exit() used later in the program.

list=[1,2,3,4]
it = iter(list) # this builds an iterator object
print (next(it)) #prints next available element in iterator 

#Iterator object can be traversed using regular for statement
for x in it:
 print (x, end=" ")

#or using next() function
while True:
 try:
  print (next(it))
 except StopIteration:
  sys.exit() 
 #you have to import sys module for this
