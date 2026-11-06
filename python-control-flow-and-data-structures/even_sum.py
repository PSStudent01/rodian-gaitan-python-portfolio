# 1) For Loop:
# This writes a script to perform a 'for loop' that:
## Uses a for loop to iterate through the numbers 1 to 50.
## Calculates the sum of all even numbers in that range.
## Prints the result as: "The sum of even numbers from 1 to 50 is X." (where X is the calculated sum).

even_sum = 0 

for num in range(1, 51): # 'for loop' iterates through the numbers 1 to 50.
                        # to create a range of 1 to 50, the start needs to be 1 and the stop needs to be 51
    if num % 2 == 0:    # 1) conditional structure checks for even integers, and if integer is even...
        even_sum += num # 2) ...it adds integer to current integer sum/count.
print(f"The sum of even numbers from 1 to 50 is {even_sum}.")


# 2) While Loop:
# Modifying the script to perform the same task using a 'while loop' instead of a 'for loop':

num = 1  # variable 'num' declared and initialized to start count number at 1
even_sum = 0 # variable 'even_sum' declared and initialized to start tracking the total sum

while num != 51: # while loop indicating to run iterations for as long as 'num' is not equal to 51
    if num % 2 == 0: # and at each iteration, if 'num' is an even number then...
        even_sum += num # ...add such number to total being tracked by variable 'even_sum'
    num += 1 # manual bump up at each iteration, by a step of 1
print(f"The sum of even numbers from 1 to 50 is {even_sum}.") # positioned the print() function in far left, ALONGSIDE to the 
                                                              # 'While' loop (and not WITHIN the loop) so that ONLY and ONLY
                                                              # when the loop completes, will it print the message stated.
                                                              # If you place it WITHIN the 'While loop' or WITHIN the 'If conditional
                                                              # structure', it will execute according to each of those. 

'''
Takeaway:
- Both loop versions produce the same result. However, I found the 'For Loop' to be more beneficial in this case, because:
-- it lets you use the 'range()' function, which I think gives you a bit more control on which numbers are processed. 
-- it also bumps the count/number or whatever is being counted/tracked automatically, whereas using the While loop, you'd 
have to establish that step manually, for example: "num += 1"
-- Also forgetting 'num += 1' will cause an infinite loop.
'''



