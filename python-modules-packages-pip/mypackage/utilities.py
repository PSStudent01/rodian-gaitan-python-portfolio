
''' 
Small utility functions packaged as part of mypackage
'''

import math

# Returns a greeting string for a given name:
def greet(name):  
    return (f"Hello {name}!")

# Returns the factorial of n:
def factorial(n): 
    return math.factorial(n) # Returns n! (n must be a non-negative whole number)

if __name__ == "__main__":
    # quick self-test; runs only when this file is executed directly, not when imported
    print(greet("Rod"))
    print(factorial(5))

