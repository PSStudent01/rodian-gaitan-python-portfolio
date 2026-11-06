'''
Multiplier closure demo.
make_multiplier(factor) returns a function that multiplies its input by factor. The returned function is a closure: it remembers 
factor even after make_multiplier has finished running.
'''

def make_multiplier(factor):    
    def multiply(x): # Inner function that uses 'factor' from the enclosing function 'make_multiplier()'.
        return x * factor # Accesses the enclosing function's variable 'factor'. This allows the returned function to retain 
                          # access to that value.
    return multiply  # Returns the inner function itself (without parentheses), rather than calling it. This allows the function
                    # to be used after make_multiplier() finishes executing.

times3 = make_multiplier(3) # a function that remembers factor=3
times10 = make_multiplier(10) # a separate function that remembers factor=10

# More polished:
print()
## Shows closures produce the expected results:
print("Shows closures produce the expected results:")
print(f"times3(7) = {times3(7)}")      # times3(7) = 21
print(f"times10(7) = {times10(7)} \n")    # times10(7) = 70

## Shows each closure keeps its own factor across multiple calls, in other words, "retains the factor":
print("Shows each closure keeps its own factor across multiple calls, in other words, 'retains the factor':")
print(f"times3(5) = {times3(5)}")     # 15
print(f"times10(5) = {times10(5)} \n")   # 50

## Edge cases. These show it works with zero, negatives, and decimals:
print("Edge cases. These show it works with zero, negatives, and decimals:")
print(f"times3(0) = {times3(0)}")        # 0
print(f"times3(-4) = {times3(-4)}")      # -12
print(f"times10(2.5) = {times10(2.5)} \n")  # 25.0

## This shows make_multiplier can create as many independent closures as you like:
print("This shows make_multiplier can create as many independent closures as you like:")
times0 = make_multiplier(0)
print(f"times0(99) = {times0(99)}")      # 0


