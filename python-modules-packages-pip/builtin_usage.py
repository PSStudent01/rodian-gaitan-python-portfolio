'''Uses the math, random and platform modules to print a random number, its floored square root, the OS, and the Python version.'''

# Imports the math, random, and platform modules:
import math, random, platform 

# Generates a random integer between 1 and 100 using the random module:
random_num = random.randint(1, 100)
print(f"Random Number: {random_num}")

# Calculates the square root of random_num, rounds it down to the nearest integer using math.floor(), and prints the result:
sqrt_num = math.floor(math.sqrt(random_num)) 
print(f"Square root of {random_num}: {sqrt_num} (floored)")

# Retrieves and prints the system's OS name and Python version using functions from the platform module:
## System's OS name:
os_name = platform.system()
print(f"Operating System: {os_name}")
## Python version:
py_version = platform.python_version()
print(f"Python Version: {py_version}")

