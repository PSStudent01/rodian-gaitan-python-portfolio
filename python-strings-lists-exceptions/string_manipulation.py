
'''
String manipulation demo.
Asks for a sentence, then prints it in uppercase, reversed, with its vowel
count, and with spaces replaced by hyphens.
'''

new_string = "" # 'new_string' starts empty
result = "" # 'result' starts empty

# Asks for a sentence, then prints it in uppercase, reversed:
string = input("Enter a sentence: ") # Prompts the user to enter a sentence.

string = string.upper() # Converts the entire sentence to uppercase and stores it in variable 'string'.
print("Uppercase: ", end = "") # 1b) ...then pulls value from 'string' variable below up onto the same line as 'Uppercase:' string.
print(string) # 1a) prints the value from 'string' variable...
print("Reversed: ", end = "") # 2b) ...then pulls value from 'string' variable below up onto the same line as 'Reversed: ' string.
print(string[::-1]) # 2a) prints the sentence in reverse order...


# Calculates total count of vowels in string:
for letter in string: # iterates through each letter in string
    if letter.lower() in "aeiou": # then checks to see if each letter (lower caseo or not) is a vowel.
        new_string = new_string + letter # and if the letter being evaluated is a vowel, it gets added to the 'new_list' without
                                        # replacing any of the existing letters in the list.
print("Total count of vowels in string: ", end = "") # 3b) ...then pulls value from 'new_string' variable below up onto the same line as
                                                     # "Total count of vowels in string: " string
print(len(new_string)) # 3a) prints the current count of 'new_string'...


# Replaces every space in the sentence string with a hyphen (-) and prints the modified string:
for letter in string:  # iterates through each letter in string...
    if letter == " ": # and for every space found...
        result = result + "-" # it replaces it with hyphen (-) and stores it in 'result' vairable.
    else:
        result = result + letter # otherwise, if it's a letter it stores it in the same 'result' variable.
print("Hyphenated: ", end = "") # 4b) ...then pulls value from 'result' variable below up onto the same line as
                                # "Hyphenated: " string.
print(result) # 4a) prints the hyphened sentence version...


