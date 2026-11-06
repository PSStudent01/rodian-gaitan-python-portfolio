'''
Fibonacci generator.
gen_fibonacci(n) yields the first n Fibonacci numbers (0, 1, 1, 2, 3, 5, ...) one at a time instead of building a whole list.
'''

# Yield the first n Fibonacci numbers:
def gen_fibonacci(n):
    a = 0
    b = 1

    for i in range(n): # Repeats the loop n times, generating one Fibonacci number per iteration
        yield a  # Returns a value while preserving the function's execution state for the next iteration.
                 # Yields the current Fibonacci number and pauses execution until the next value is requested.
                 # It doesn't end the function like return does, it just pauses execution and resumes when the next value is requested.
        a, b = b, a + b # Updates both variables simultaneously: a becomes the previous b, and b becomes the sum of the previous 
                        # a and b.

# print(gen_fibonacci(12)) # Returns a generator object rather than displaying the Fibonacci numbers.
                           

print("First 12 Fibonacci numbers:")

for number in gen_fibonacci(12):
    print(number, end=" ") # Returns: 0 1 1 2 3 5 8 13 21 34 55 89

print()


