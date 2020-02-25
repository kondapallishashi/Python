#Demonstrates nested if loops in python.
#The indentation is the most key factor while using nested ifs as {} are not used to segment the code blocks.
#Ideally two spaces are used by python, but in this program tab is used for better visibility.

num =  int(input("Enter a number: "))
if num%2==0: #Outer if loop
 if num%3==0: #Inner if loop
    print ("Divisible by 3 and 2")
 else: #Else in inner if loop
    print ("divisible by 2 not divisible by 3")
else: #Else in outer if loop
    if num%3==0: #if in else block of outer loop
        print ("divisible by 3 not divisible by 2")
    else: #else belonging to the above if loop but outer else block.
        print ("not Divisible by 2 not divisible by 3")

