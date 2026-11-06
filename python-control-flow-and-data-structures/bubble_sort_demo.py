
"""Bubble sort demo.
Sorts a list of integers using nested loops, swapping adjacent values that are out of order, and prints the list after each pass.
"""

nums = [64, 25, 12, 22, 11] # declared & initialized a list called 'nums'
print("Original list:", nums)  # prints the list 'nums' as the original list

for i in range(len(nums) - 1):  # outer loop: one pass per iteration.
                                # 1) counts the number of items in 'nums', minus 1, then for every number in that range, it does 
                                # the following...
    for j in range(len(nums) - 1 - i):  # inner loop: compares adjacent pairs
                                        # 2) counts the number of items in 'nums', minus the passes already completed then for 
                                        # every number in that range, it does the following...
        if nums[j] > nums[j + 1]: # If the left neighbor is bigger than the right neighbor, the pair is out of order and needs 
                                  # to be swapped.
            nums[j], nums[j + 1] = nums[j + 1], nums[j]  # Swap the two values in one line (Python's tuple swap).
    print(f"After pass {i + 1}:", nums)  # inside outer loop, outside inner loop

print("Sorted list:", nums)    # prints sorted list