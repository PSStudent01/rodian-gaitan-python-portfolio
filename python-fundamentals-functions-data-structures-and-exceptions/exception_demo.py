"""Exception demo.
Shows how to raise and catch exceptions. safe_divide() raises a ValueError when the divisor is zero. A loop calls it with 
several test values and catches the ValueError with try/except, printing the message stored in the exception.
A finally clause prints "Division operation completed" after every attempt, whether or not an error occurred. A last demo 
catches a generic Exception raised by converting an invalid string with int().
"""

## A function 'safe_divide(a, b)' that returns the result of a / b, and raises a ValueError with a message like 
## “Cannot divide by zero” when b is zero.

def safe_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

## Using a 'try/except' structure to call 'safe_divide' with some test values that include a zero divisor. Then catches the 
## 'ValueError' exception and prints a friendlier error message to the user.

test_values = [(15, 3), (10, 5), (10, 0), (3, 0), (8, 0)]

for a, b in test_values: # iterates through each and every pair of values of each and every tuple. IOWs, unpacks each tuple 
                         # into a and b.
    try:
        print(safe_divide(a, b)) # and then calls the function 'safe_divide(a, b)' to work with both values of each tuple.
                                 # while simultanously printing the result of the function acting on the value pair of each tuple
                                 # IOWs, calls the function and prints its result.
    except ValueError as e: # this catches the exception when a division by zero takes places and then...
        print(f"Warning: {e}") # uses the exception ('e') that I created earlier to print the warning message
                                # IOWs, 'e' refers to the caught exception object.
    
## Including a finally clause in the try/except that prints a message like “Division operation completed” whether or not an error
##  occurred.
    finally:
        print("Division operation completed")

## Also demonstrating catching a generic exception by performing an unsafe operation (for example, converting an invalid string 
## to int in a try block) and catching the generic Exception to print a message.
try:
    number = int("abc")
    print(number)
except Exception as e:
    print(f"A generic exception was caught: {e}")


