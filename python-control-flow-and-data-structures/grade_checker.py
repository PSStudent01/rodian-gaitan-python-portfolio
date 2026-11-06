"""Grade checker:
Asks for a numeric score from 0 to 100 and re-prompts until the input is valid. Converts the score to a letter grade (A-F) with 
an if-elif-else chain and prints a pass or retake message. Passing is a C or better (70+).
"""

def get_score():
    # Prompt until the user enters a whole number from 0 to 100.
    while True:
        try:
            score = int(input("Please enter your score(0-100): ")) # asks the user to input a numeric grade (0-100) and casts it to int 
                                                                   # data type. Then stores the data into variable 'score'.
            #break # commented out and replaced with 'continue' below in order to allow to also check for "if 0 <= score <= 100:"
                   # continue retries after bad input, and return is what exits on success.
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if 0 <= score <= 100:
            return score
        else:
            print("Score must be between 0 and 100.")


score = get_score()  # catches the value the function returns and stores it in 'score'; calling get_score() alone would 
                        # discard it.

    
# if-elif-else structure to convert the score to a letter grade based on a typical scale and render a message depending on grade:
if score <= 100 and score > 89: 
    print("Your grade is: A") 
elif score <= 89 and score > 79:
    print("Your grade is: B")
elif score <= 79 and score > 69:
    print("Your grade is: C") 
elif score <= 69 and score > 59:
    print("Your grade is: D") 
#elif score <= 59 and score >= 0:
#   print("Your grade is: F") 
else:
    print("Your grade is: F") 


# final message so that if the grade is passing (A-C),it congratulates the user. Otherwise if it is a D or F, it 
# encourages the user to retake the coourse).
if score <= 100 and score > 69:
    print("Congrats, you've passed the course!")
else:
    print("Unfortunately, you'll need to retake the course!")








