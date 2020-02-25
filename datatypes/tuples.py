#Demonstrates the usage of tuple data types in python.
#tuple is similar to list, but unlike lists elements cannot be added or updated.
#Elements in lists are enclosed in [] and elements in tuples are enclosed in ()

fruits = ("apples", 40, "grapes", "25.8", "mangoes", 55)
exotic_fruits = ("kiwi", 200)

#Printing the entire list
print("The full fruit tuple is: ",fruits)
#printing the first element in the list fruits
print("The first element in the fruit tuple is ", fruits[0])
print("The last element in the fruit list is ", fruits[-1])
print("The list elements from 3rd element to the last element ", fruits[2:])
print("The list of elements from 3rd to 5th element in the fruit list ", fruits[2:4])
print("To repeat the list of elements twice, use repeatitor operator * ", fruits * 2)
print("To add another list exotic_fruits to the fruits list, use + operator ", fruits + exotic_fruits)

#The elements in the tuple cannot be updated. Uncomment the below line and review the error.
#fruits[5] = 60
print("The updated fruits list is ", fruits)
