#Demonstrates the usage of assets in python programs

# Asserts are like sanity checks, which raise an exception if the expression is evaluated to false.
# Introduced in python 1.5, assertions are usually places at the start of the function to check the validity of input and immediately after the function call to check the validity of output.

#If the expression is false, AssertionError is raised and can be handled by try-except statement.

#Syntax: assert Expression[, Arguments]


#Define a function to convert temperature from kelvin format to fareinheit

def KelvinToFahrenheit ( Temperature ) :
    assert(Temperature >= 0), "Colder than sub zero."
    return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))