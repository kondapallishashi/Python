#Python supports single line statements and statements end at the end of the line
#python does not need ; at the end of statements and when used throws a warning

##print("Hello World");

#Multi-line statements can be written in a single line separated by ; as long as a new block is not being started in the same line.
print("Hellow World"); print("This statement follows in the same line separated by semi-colon"); print("this as well")

#In case there is a need for a statement to extend to multi lines use the \ operator to indicate that the next line is an extension
#Remove the \ operator at the end of the statement and see the error
print("This line is extended  \
to multiple lines \
using the \ operator. Remove the \ at the end of each statement \
and observe the error")

#However the statements between [], {} and () do not need the operator \ to extend it to multiple lines.
#
days = ["Monday", "Tuesday", 
        "Wednesday", "Thursday", "Friday",
        "Saturday"]
print(days)
