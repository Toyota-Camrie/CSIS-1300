'''This code goes through a string
entered by input to see if it is
a palindrome'''

# ---------------------------------------
# Camrie Campos
# CSIS 1300 Spring 2023
# Midterm Exam Part 2
# Due February 25, 2023
# ---------------------------------------

# ---------------------------------------
# CREATIVE ELEMENT
# Ask user for their birthdate
# and see if their birthdate is a
# palindrome
# ---------------------------------------

# Ask user for a word or phrase
word = input("\n\nEnter a word or phrase (no " +
             "end punctuation please - .?!): ")

# Set new string to lowercase version of
# user input
final = word
final = word.lower()

# Get rid of separators in new string
# if any are present
final = word.replace(" ", "")
final = word.replace("'", "")
final = word.replace(", ", "")

# Initialize boolean and integer
# (integer used for last values in
# string)
isPal = False

compare = final[::-1]

# Use for loop to iterate through
# string to find if each character
# matches with the "end" character
if final == compare:
    isPal = True

# Print result to user using boolean
if isPal is True:
    print(word + " is a palindrome.")
else:
    print(word + " is not a palindrome.")


# CREATIVE ELEMENT HERE
date = input("\nPlease enter your birthdate in MM-DD-YYYY format: ")

birth = date
# Remove hyphens
birth = date.replace("-", "")

# Initialize boolean and integer
# (integer used for last values in
# string)
pal = False

mate = birth[::-1]

# Use for loop to iterate through
# string to find if each character
# matches with the "end" character
if birth == mate:
    pal = True

# Print result to user using boolean
if pal is True:
    print("Your birthdate " + date + " is a palindrome.")
else:
    print("Your birthdate " + date + " is not a palindrome.")
