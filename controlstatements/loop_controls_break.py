#demonstrate break statement
for letter in 'Python': # First Example
 if letter == 'h':
  break
 print ('Current Letter :', letter)

var = 10 # Second Example
while var > 0:
 print ('Current variable value :', var)
 var = var -1
 if var == 5:
  break


no=int(input('any number: '))
numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
 if num==no:
  print ('number found in list')
 break
else:
 print ('number not found in list')