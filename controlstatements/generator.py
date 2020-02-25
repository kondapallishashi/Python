#Demonstrates generator object in python.
#A generator is a function that produces or yields a sequence of values using yield method.
#When a generator function is called, it returns a generator object without even beginning
#execution of the function. When the next() method is called for the first time, the function
#starts executing, until it reaches the yield statement, which returns the yielded value. The
#yield keeps track i.e. remembers the last execution and the second next() call continues
#from previous value.

import sys
def fibonacci(n): #generator function
 a, b, counter = 0, 1, 0
 while True:
  if (counter > n):
   return
  yield a
  a, b = b, a + b
  counter += 1
f = fibonacci(5) #f is iterator object

while True:
 try:
  print (next(f), end=" ")
 except StopIteration:
  sys.exit()