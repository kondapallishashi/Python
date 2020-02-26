#Demonstrates the built in functions that can be used with tuples.

#DEFINING TUPLES

# Defining a tuple. Tuples are defined using the ().
# Tuple with numerical Data
nums = (1,2,3,5,6,8,9)
# Tuple with string data type
fruits = ("mangoes", "grapes", "bananas", "apples")
# Tuple with mixed data types
employee = (150, "Sasi", "Delivery", 30000, 1978, "India")
# empty tuple can be defined that we can add elements later on.
noelement = ()
# Tuples with single elements need to have comma added after them
singleElement = (25,)

# any list of elements with out enclosing delimiters such as [] for lists () for tuples {} for dictionaries default to tuple
nodelim = 23,45, 67, 87, 39


# ACCESSING ELEMENTS OF TUPLES

# accessing First element of tuple. Tuple indexing starts with 0.
print("The first element of Tuples nums, fruits, employee: ", nums[0], fruits[0], employee[0] )

# Accessing the last element of tuples. -ve indexing allows accessing the elements from the end. -1, -2 etc
print("The last element of Tuples nums, fruits, employee: ", nums[-1], fruits[-1], employee[-1] )

# Accessing the elements using the slice operator [:]
print("The second to the last element of nums tuple: ", nums[1:])
print("The third to the last element of fruits tuple: ", nums[:2])
print("The third to the last element of fruits tuple: ", nums[2:4])

# UPDATING THE VALUES OF TUPLES ARE NOT SUPPORTED. TUPLES ARE LIKE READ ONLY LISTS.
# This throws an error. Uncomment and test.
# nums[0] = 25

# new tuples can be formed by taking different tuples or subset of tuples and adding them.
# multiple tuples can be defined in the same line as shown below.
testTuple1, testTuple2 = (1,3,5), (2,4,6)
 
# Tuples can be concatenated using the + operator to form new tuples.
testTuple = testTuple1 + testTuple2
print("new tuple formed by adding testTuple1 and testTuple2 is: ", testTuple)

# The entire tuple can be deleted using del

del testTuple2
# After del the testTuple2 does not have any references, so printing it would throuw a run time error. 
# uncomment and test.
#print(testTuple2)

# The * operator can be used to repeat the elements of the tuple.
print(" The elements of testTuple1 repeated 3 times :", testTuple1 * 3)

# Membership of an element can be found using the in operator.
print("testTuple contains the element 4 : ", 4 in testTuple)
print("testTuple contains the element 100 : ", 100 in testTuple)

# cmp(tuple1, tuple2) - No longer available in python 3


# len(tuple)
print(" The length of the testTuple is", len(testTuple))

# max(tuple)
print("The max value of the fruits tuple is: ", max(fruits))
print("The max value of the nums tuple is: ", max(nums))
# This will throw a runtime error as the data types are of mixed type.
print("The max value of the employee tuple is: ", max(employee))

# min(tuple)
print("The min value of the fruits tuple is: ", min(fruits))
print("The min value of the nums tuple is: ", min(nums))
# This will throw a runtime error as the data types are of mixed type.
print("The min value of the employee tuple is: ", min(employee))

# tuple(seq) - converts a list to tuple.
list1 = ["apples", 40, "grapes", 30, "bananas", 20]
rates = tuple(list1)
print("The tuple created from the list using the tuple() method is ", rates)





