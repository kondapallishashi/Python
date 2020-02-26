#Demonstrates the built-in functions for operations on Lists.
# Covers

#DEFINING THE LISTS

#ACCESSING VALUES IN LISTS

# FUNCTIONS COVERED IN THIS PROGRAM
# cmp(list1, list2) - Deprecated in Python 3.1
# len(list)
# max(list)
# min(list)
# list(seq)

# Defining the lists.
list1 = ["apples", 80, "grapes", 40, "mangoes", 60, "bananas", 20]
list2 = [1,2,3,4,5,6]
list3 = ["a","b","c","d","e","f"]

#Elements can be accessed using index values. Indexing starts from 0 to n-1 where n is the number of elements.

# To Access the first element.
print("The first element of ", list1, " accessed using list[0] is: ", list1[0])
# To Access the last element
print("The last element of ", list1, " accessed using list[-1] is: ", list1[-1])
# To List the elements from 3rd element to the end of the list.
print("The elements from 3rd element to the end of the list: ", list1, " accessed using list[3:] is: ", list1[3:])
print("The elements from 3rd element to the end of the list: ", list2, " accessed using list[3:] is: ", list2[3:])
print("The elements from 3rd element to the end of the list: ", list3, " accessed using list[3:] is: ", list3[3:])

print("The elements from start to the 3nd element of the list: ", list1, " accessed using list[:2] is: ", list1[:2])
print("The elements from start to the 2nd element of the list:: ", list2, " accessed using list[:2] is: ", list2[:2])
print("The elements from start to the 2nd element of the list: ", list3, " accessed using list[:2] is: ", list3[:2])

print("The elements from start index to the end index of the list: ", list1, " accessed using list[2:5] is: ", list1[2:5])
print("The elements from start index to the end index of the list: ", list2, " accessed using list[1:4] is: ", list2[1:4])
print("The elements from start index to the end index of the list:", list3, " accessed using list[1:3] is: ", list3[1:3])

#Updating the elements of the list.
#To update access the element of the list and assign new value.

list1[1] = 65
print("The Updated list ", list1)

#Define multiple lists in the same line.
list4, list5 = [1,2,3], [7,8,9]

# Multiple operators can be used with lists

#Adding the lists using the + operator
print("The concatenated list of ", list4, " and ", list5, " is ", list4+list5)
#len(list) is used to get the length or size of the list.
print("length of the list ", list1, "is ", len(list1))

#using * to repeat the elements of the list
print("The list ", list4, "repeated twice using *2 is ", list4*2)

# in can be used to determine membership.
print("to determine if an element 3 is existing in ", list4, 3 in list4)

#max(list) can be used to identify the element with maximum value.
# When the list is of mixed data type, say int and str, the function will throw a runtime error.
print("The maximum value of list :", list1, " is: ", max(list2))
#min(list) can be used to identify the element with minimum value.
# When the list is of mixed data type, say int and str, the function will throw a runtime error.
print("The minimum value of list :", list1, " is: ", min(list2))

# Lists can be created using the list(seq) function. The seq can be a tuple or a string.
# making a list from a tuple.
tuple1 = ("france", "germany","USA", "greece", "india")
countries = list(tuple1)
print("The list made out of tuple ", tuple1, " is: ", countries)

#Making a list from a string
vowels = 'aeiou'
list_vowels = list(vowels)
print("The list made out of string: ", vowels, "is :", list_vowels)


# list.append(obj)
# This method does not return any value but appends the obj to the end of the list.
# append() takes exactly one argument. provising more than one will throw a runtime error.
list1.append("kiwi")
print("The updates list is:", list1)
# Adding another list as a whole to the original list using the append.
list1.append(list2)
print("The updates list is:", list1)

# list.extend(seq)
# Adding the elements in the seq to the list. 
testList = [2,4,6,2,8,2,6,10]
addonList = [21,25,31,38]
print("The list ", testList, "is extended with ", addonList, "using the extend(): ", testList.extend(addonList))

# list.count(obj)
# The count() method provides the number of times the obj appeared in the list.

print("The count of 2 in ", testList, " is: ", testList.count(2))
print("The count of 12 in ", testList, " is: ", testList.count(12))

# list.index(obj)
# this method returns the lowest index at which object appears.
print(" The index at which 2 appears in ", testList, " is: ", testList.index(2))
print(" The index at which 6 appears in ", testList, " is: ", testList.index(6))
# trying to index an element that is not in list throws a runtime error. Uncomment below line and test.
# print(" The index at which 100 appears in ", testList, " is: ", testList.index(100))

# list.insert(index,obj)
# insert() method inserts the object at the specified index.
testList.insert(100,3)
print("The updated list after inserting 100 at index 3 is: ", testList)


#list.pop(obj = list[-1])
# This method removes the object from the list. Default is the last element of the list.
# index of the list is passed as parameter to this method. 
# This method returns the object removed.
print("The original elements of the list: ", testList)
removedObj = testList.pop()
print("The updated list is: ", testList, "The removed object is: ", removedObj)

#index can be specified while removing the object.
removedObj = testList.pop(-2)
print("The updated list is: ", testList, "The removed object is: ", removedObj)

#list.remove(obj)
# this method removes the object from the list
# This method does not return any value.
print("The original elements of the list: ", testList)
testList.remove(21)
print("The updated list is after removing element 21 : ", testList)

#list.reverse()
# this method reverses the order of elements in the list.
# this method does not return any values.
print("The original elements of the list: ", testList)
testList.reverse()
print("The list after elements of the list are reversed using list.reverse(): ", testList)

#list.sort([func])
# This method sorts the elements of the list. Does not return any value.
testList.sort()
print("The sorted elements of the list: ", testList)







