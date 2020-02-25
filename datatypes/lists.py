#Demonstrates the usage of list data type in python.
#lists are a versatile compound data types that can contain multiple elements of different data types, separated by commas
#Elements are indexed from 0 to -1 till the end
#elements can be accessed using the [] with index number or slicing operator [start:end]

fruits = ["apples", 40, "grapes", "25.8", "mangoes", 55]
exotic_fruits =["kiwi", 200]

#Printing the entire list
print("The full fruit list is: ",fruits)
#printing the first element in the list fruits
print("The first element in the fruit list is ", fruits[0])
print("The last element in the fruit list is ", fruits[-1])
print("The list elements from 3rd element to the last element ", fruits[2:])
print("The list of elements from 3rd to 5th element in the fruit list ", fruits[2:4])
print("To repeat the list of elements twice, use repeatitor operator * ", fruits * 2)
print("To add another list exotic_fruits to the fruits list, use + operator ", fruits + exotic_fruits)

#Update the elements in the list
#fruits[5] = 60
#Since the fruits tuple is not updated, this will print the old tuple itself
print("The updated fruits list is ", fruits)
