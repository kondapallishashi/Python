#Demonstrates the membership operators in, not in python.
#Membership operators in, not in tests whether the element exists in sequence such as strings, lists or tuples.
# in returns 1 if element exists in sequence or 0 if it does not exist

# not in returns 0 if element exists in sequence or 1 if it does not exist

text = "This is a sentence with some key words for us to search"

#searching a word in a sentence. Change the word and test.
word = "This"
if(word in text):
    print("The word", word, " exists in sentence", text)
else:
    print("The word", word, " does not exist in sentence", text)

#Checking if the number is in a list. Change the number and test again.
num_list = [2,4,6,8,10]
num = 6

if(num in num_list):
    print("The number is in the list", num_list)
else:
    print("The number is not in the list", num_list)

# not in works exactly like in but with opposing results.
#Change num value and test again.
if(num not in num_list):
    print("The number is in the list", num_list)
else:
    print("The number is not in the list", num_list)

