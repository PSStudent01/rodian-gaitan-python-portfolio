
'''
Demonstrates importing a custom module from a package.
'''

from mypackage import utilities

print(utilities.greet('Rod'))
print(f"The factorial of 5 is {utilities.factorial(5)}") 
