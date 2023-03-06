'''This program mimicks the Soundex
System by encoding a word into a letter
followed by three numbers that roughly
describe how the word sounds
'''

# ----------------------------------
# Camrie Campos
# CSIS-1300 Spring 2023
# Coding Four Assignment
# February 8, 2023
# Due February 14, 2023
# ----------------------------------

# ----------------------------------
# CREATIVE ELEMENT
# Take the reverse of the word
# given by the user and then
# return the encoding of
# the reversed string
# ----------------------------------

# Initialize variables
encode = ""
reverse = ""
rev_encode = ""
last = ""

# Ask user to type in a word
word = input("\n\nPlease type in a word: ")

# Add reversed word to string
# and add first character of
# reversed string to reverse
# encoding after capitalizing
reverse = word[::-1]
reverse = reverse.capitalize()
rev_encode = reverse[0]


# Capitalize original word
word = word.capitalize()

# Add first character of word to
# string for encoding of word
encode = word[0]

# Work with every character in word
# except for the first character
word = word[1:]


# Word with every character
# in reversed word except first
reverse = reverse[1:]

# Use replace() method to replace
# a, e, i, o, u, h, y, and w
# from word
word = word.replace("a", "")
word = word.replace("e", "")
word = word.replace("i", "")
word = word.replace("o", "")
word = word.replace("u", "")
word = word.replace("h", "")
word = word.replace("y", "")
word = word.replace("w", "")


# Use replace() method to replace
# a, e, i, o, u, h, y, and w
# from reversed word
reverse = reverse.replace("a", "")
reverse = reverse.replace("e", "")
reverse = reverse.replace("i", "")
reverse = reverse.replace("o", "")
reverse = reverse.replace("u", "")
reverse = reverse.replace("h", "")
reverse = reverse.replace("y", "")
reverse = reverse.replace("w", "")


# Use a for loop with nested if
# statements to iterate through
# word and add the appropriate
# numbers for encoding
for letter in word:

    # First if statement
    # replaces all occurrences of
    # b, f, p, and v with 1 (no repeats)
    if letter in "bfpv" and last != '1':
        encode += '1'
        last = '1'

    # End of first if statement

    # Replaces all occurrences of
    # c, g, j, k, q, s, x, and z
    # with 2 (no repeats)
    if letter in "cgjkqsxz" and last != '2':
        encode += '2'
        last = '2'

    # End of second if statement

    # Replaces all occurrences of
    # d and t with 3 (no repeats)
    if letter in "dt" and last != "3":
        encode += "3"
        last = "3"

    # End of third if statement

    # Replaces all occurrences of
    # l (el) with 4 (no repeats)
    if letter in "l" and last != "4":
        encode += "4"
        last = "4"

    # End of fourth if statement

    # Replaces all occurrences of
    # m and n with 5 (no repeats)
    if letter in "mn" and last != "5":
        encode += "5"
        last = "5"

    # End of fifth if statement

    # Replaces all occurrences of
    # r with 6 (no repeats)
    if letter in "r" and last != "6":
        encode += "6"
        last = "6"

    # End of last if statement

# End of for loop


# Set string equal to ""
# for reverse encoding process
last = ""

# Use a for loop with nested if
# statements to iterate through
# reversed word and add the
# appropriate numbers for encoding
for c in reverse:

    # First if statement
    # replaces all occurrences of
    # b, f, p, and v with 1 (no repeats)
    if c in "bfpv" and last != '1':
        rev_encode += '1'
        last = '1'

    # End of if statement

    # Replaces all occurrences of
    # c, g, j, k, q, s, x, and z
    # with 2 (no repeats)
    if c in "cgjkqsxz" and last != '2':
        rev_encode += '2'
        last = '2'

    # End of if statement

    # Replaces all occurrences of
    # d and t with 3 (no repeats)
    if c in "dt" and last != "3":
        rev_encode += "3"
        last = "3"

    # End of if statement

    # Replaces all occurrences of
    # l (el) with 4 (no repeats)
    if c in "l" and last != "4":
        rev_encode += "4"
        last = "4"

    # End of if statement

    # Replaces all occurrences of
    # m and n with 5 (no repeats)
    if c in "mn" and last != "5":
        rev_encode += "5"
        last = "5"

    # End of if statement

    # Replaces all occurrences of
    # r with 6 (no repeats)
    if c in "r" and last != "6":
        rev_encode += "6"
        last = "6"

    # End of if statement

# End of for loop


# If length of encoded word is greater than 4
# get rid of all characters that come
# after the 4th character
if len(encode) > 4:
    encode = encode[0:4]

# Add zeros for all of the spaces
# left over if there aren't four
# characters total
if len(encode) == 3:
    encode += "0"

if len(encode) == 2:
    encode += "00"

if len(encode) == 1:
    encode += "000"


# If length of reverse encoded word
# is greater than 4
# get rid of all characters that come
# after the 4th character
if len(rev_encode) > 4:
    rev_encode = rev_encode[0:4]

# Add zeros for all of the spaces
# left over if there aren't four
# characters total
if len(rev_encode) == 3:
    rev_encode += "0"

if len(rev_encode) == 2:
    rev_encode += "00"

if len(rev_encode) == 1:
    rev_encode += "000"


# Print encoded word to user
print("Your encoded word is: ", encode)

# Print reversed encoding to user
print("The reverse encoding of your word is: ", rev_encode)

# -------------------------------------------
# THOUGHTS
# I thought this program was pretty creative.
# I had asked for help with this program,
# but I was frustrated to learn that I had
# to redo the code I had initially done
# to take into account one of the requirements
# for this program. I only wish I could've
# figured out a way to have that
# requirement in addition to the initial code.
# -------------------------------------------
