
#The range(5) provides an iteration of sequential numbers with range from 0 to 5.
for var in list(range(5)):
    print (var)

for letter in 'Python': # traversal of a string sequence
 print ('Current Letter :', letter)
print()
fruits = ['banana', 'apple', 'mango']
for fruit in fruits: # traversal of List sequence
 print ('Current fruit :', fruit)

 #iterating using the sequence index
 fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
 print ('Current fruit :', fruits[index])

 #using else with for loop
 numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
 if num%2==0:
  print ('the list contains an even number')
 break
else:
 print ('the list doesnot contain even number')


 #Nested for loop
 #the end='' is used to indicate that instead if a new line character after the print statement, use a space character
 for i in range(1,11):
    for j in range(1,11):
        k=i*j
        print (k, end=' ')
 print()