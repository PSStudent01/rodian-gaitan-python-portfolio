
'''Age validator.   
validate_age() raises a ValueError for any age outside 0-120. The script
asks for an age and reports whether it was accepted or why it was rejected.
'''

def validate_age(age):
    try:
        if age >= 0 and age <= 120:
            print("Age is accepted!")
    except ValueError:  
        print("Invalid input: Enter age as a whole number")

# Raising an exception specifically for when age is outside of range, rather than using 'else' statement:
def check_age(age):
    if not (age >= 0 and age <= 120):
        raise ValueError("Age must be between 0 and 120 (inclusive).")

def main():
    try:
        age = int(input("Enter age: "))
        validate_age(age)  
        check_age(age) 
    except ValueError as e:
        print(e)
main()

# See Original Source File for a More Complete Version! 

