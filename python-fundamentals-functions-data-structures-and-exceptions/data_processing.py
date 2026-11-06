"""Data processing.
Calculates the average grade for each course in a dictionary of grade tuples. get_average_grade() uses try/except to handle an \
empty tuple (division by zero) and returns None in that case, so the loop can report "not available" instead of crashing. One 
course intentionally has no grades, to show that the exception handling works.
"""

# Defining a function 'get_average_grade(grades_tuple)' that takes a tuple of numeric grades and returns the average:
grades_tuple = (78, 85, 98, 52, 75, 92) # 1) defining/declaring tuple 'grades_tuple'

def get_average_grade(grades_tuple): # 2) declaring function 'get_average_grade' to receive values for tuple 'grades_tuple's
    try: # 5a) try/except block build
        return sum(grades_tuple) / len(grades_tuple)# 3) calculates their total sum; then divides it by total count of numbers
                                                    # in the tuple to get the average; and then returns the avg.
    except ZeroDivisionError: # 5b) try/except block build
        # Handle the empty-tuple case instead of crashing
        print("Warning: cannot calculate an average of an empty tuple.") # 5c) try/except block build
        return None # 5d) # try/except block build

print(get_average_grade(grades_tuple)) # 4) calls the function "get_average_grade()" while passing it the 'grades_tuple' and 
                                       # simultaneously printing the results.
                                       # Rendering: 80.0 as the avg of all 6 numbers in the tuple

# Handling Exception for 'get_average_grade' with empty argument:
result = get_average_grade(()) # stored the returned value from a 'get_average_grade' function call with empty argument
if result is None:
    print("Average: not available (no grades to average)")
else:
    print("Average:", result)
print()

###########################################################################################################################

## Defining a dictionary 'course_grades' where keys are course names (e.g., “Math”, “Science”, “History”) and values are tuples of grades.
grades_tuple1 = (78, 85, 98, 52, 75, 92) # assigning 1st tuple to variable "grades_tuple1", to make tuple indirectly available
grades_tuple2 = (88, 91, 67, 74, 83, 95) # assigning 2nd tuple to variable "grades_tuple2", to make tuple indirectly available
grades_tuple3 = (60, 72, 89, 94, 55, 81) # assigning 3rd tuple to variable "grades_tuple3", to make tuple indirectly available
grades_tuple4 = () ### EDGE CASE tuple ###: course having an empty tuple of grades, to demonstrate your exception handling works.

course_grades = {  # Defining dictionary 'course_grades' with...
     "Math": grades_tuple1,  # key 'Math' and tuple value 'grades_tuple1'  
     "Science": grades_tuple2,  # key 'Science' and tuple value 'grades_tuple2'  
     "History": grades_tuple3,  # key 'History' and tuple value 'grades_tuple3'   
     "EdgeCase1": grades_tuple4 ### EDGE CASE dictionary item ###: key 'EdgeCase1' and tuple value 'grades_tuple4'  
}

###########################################################################################################################

## Using a loop to iterate over course_grades. For each course, it calls function 'get_average_grade(grades_tuple)' and prints a
## message like: "The average grade for Math is 85.2". It also handles any None values or exceptions gracefully.
for i in course_grades: # loop to iterate over each key:value pair of 'course_grades' dictionary
    
    # Handling Exception for 'get_average_grade' with empty argument: 
    # Attempt to handle a None value as a result of calling a function with an empty argument.
    average = get_average_grade(course_grades[i])   # call once, store the result

    if average is None:
        print(f"The average grade for {i} is not available (no grades).")
    else:
        print(f"The average grade for {i} is {average:.1f}")