#This program demonstrates the usage of if control statements.
#Python handles multiple statement blocks which for a single block of code as suites.
#complex or compound statements such as if, while, def, class etc require a header and a suite.
#header lines begin the statement with a keyword, terminate with a colon (:), followed by multiple lines of code which form the suite.

#The user inputs can be captured using input() function which returns the user input in string format.

amount = int(input("Enter an amount in between 0 and 20,00,000.00"))

# if expression: 
#   suite
if(amount < 200000):
    print("This income group is considered as low income group and is eligible for govt paid schemes")
    print("The schemes include free medical support")

#if expression: 
#   suite
# else : 
#   suite

if(amount < 500000 & amount > 200000):
    print("This income group is exempted from tax")
    print("However no schemes are applicable")
else:
    print("This income group will need to pay tax")
    print("The amount of tax will depend on multiple slabs")


amount=int(input("Enter amount: "))
if amount<1000:
 discount=amount*0.05
 print ("Discount",discount)
else:
 discount=amount*0.10
 print ("Discount",discount)

print ("Net payable:",amount-discount)



#if expression:
#   suite
# elif expression:
#   suite
# else:
#   suite

if(amount <500000):
    print("Non Taxable income group")
elif(amount > 500000 & amount < 750000):
    print("The tax applicable is 10 percent on additional amount: ", (amount-500000) * 0.1)
elif (amount >750000 & amount <1000000 ):
    print("The tax applicable is 15 percent on the additional amount:", (amount*0.15))
else:
    print("The tax applicable is 30 percent", amount*0.3)


if amount<1000:
 discount=amount*0.05
 print ("Discount",discount)
elif amount<5000:
 discount=amount*0.10
 print ("Discount",discount)
else:
 discount=amount*0.15
 print ("Discount",discount)
print ("Net payable:",amount-discount)

#single statement suites can be written in the same line without any indentation.
if("apple" == "apple") : print("Apples are same everywhere")
