'''This program looks through a word
given by the user to see if there are
three consecutive letters that are
consecutive in the alphabet.'''

# Camrie Campos
# CSIS-1300-01
# Spring 2023
# Coding Six
# March 14, 2023

# CREATIVE ELEMENT
# -----------------------
# Add creative element here
# -----------------------

def main():
    '''Main function to ask user
    for a word, call isTripleConsecutive
    function, and return output to user'''

    # Ask user for word
    threeLetters = input("Please enter a word: ")

    threeLetters.lower()

    # Call isTripleConsecutive function
    # in an if statement
    if isTripleConsecutive(threeLetters):

        # If true, print the success message
        print("There are three consecutive letters",
              " in your word that match three consecutive",
              " letters in the alphabet.")

    # If false, print the unsuccessful
    # message
    else:
        print("There is no match.")

# End of main function--------------------------------

def isTripleConsecutive(tripleLetters):
    '''This function takes a string as input
    and returns a Boolean value if the
    input string has three consecutive letters
    matching three consecutive letters
    in the alphabet'''

    # Initialize string with letters
    # of the alphabet
#    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Use a loop to iterate through
    # argument string
    for i in range(len(tripleLetters) - 2):
        if ord(tripleLetters[i]) == ord(tripleLetters[i + 1]) + 1 == ord(tripleLetters[i + 2]) + 2:
            return True
        return False

    # If there are three consecutive
    # letters in the argument that match
    # three consecutive letters in the
    # alphabet, return True

    # If there are not exactly three
    # consecutive letters matching,
    # return False

# End of isTripleConsecutive function------------------------

# Call main function
main()

# THOUGHTS
# ----------------------------
# Add thoughts here
# ----------------------------
