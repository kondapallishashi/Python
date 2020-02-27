#Demonstrates how the values passed by reference are impacted in python.
# The values are always passed by reference in python.
# ie, if the parameters are changed inside a function, the change is updated outside of the function as well.

#Function to update a list.
def updateList(lst):
    "This function updates elements in the list passed as parameter"
    lst[2] = 2
    print("The elements of lst inside the function are: ", lst)
    return

# define a list lst.
lst = [10, 20, 30, 40]

#Print the elements of the list before calling the updateList()
print("The elements of the list outside the function before calling updateList(): ", lst)

#Call the function that updates the list.
updateList(lst)

print("The elements of the list outside the function after calling updateList(): ", lst)