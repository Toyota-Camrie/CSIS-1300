'''This code takes a credit card number
and does a validation check'''

# ----------------------------------------
# Camrie Campos
# CSIS 1300 Spring 2023
# Midterm Exam Part 1
# Due February 25, 2023
# ----------------------------------------

# ----------------------------------------
# CREATIVE ELEMENT
# Change the formatting of the card number
# result at the end to be asterisks, showing
# only the last four digits of the credit
# card number entered
# ----------------------------------------

# Ask user for a 14-digit number
number = input("\n\nPlease enter the credit" +
               " card number: ")

# Add user input to a list
creditNum = [int(x) for x in number]

# Get the length of the number
length = len(str(number))

# Check if the number given is 14 digits
# using if statements (print if the
# number doesn't meet the criteria)
if length < 14:
    print("That number is not long enough.")
if length > 14:
    print("That number is too long.")

# Use a for loop to double every other digit
# after initial digit in the number
numSum = 0
for i in range(0, len(creditNum), 2):
    double = 2 * creditNum[i]

    # Use if statement to see if doubled
    # number is a two-digit number
    if double >= 10:
        double = double - 9

    # Add the new digits together (the doubles
    # digits)
    numSum += double

# End of for loop

# Initialize new variable for sum
# of other integers
newSum = 0

# Add together the rest of the digits from the
# 14-digit number using for loop
for i in range(0, len(creditNum)):
    if i % 2 == 1:
        newSum += creditNum[i]

# End of for loop

# Add together the two sums
total = newSum + numSum

# Use if statements to check if the sum is
# a multiple of 10
# then print result to user
last = str(creditNum[10:14])[1:-1]

if total % 10 == 0:
    print("The card number **** **** ** " +
          last.replace(", ", "") + " is valid.")
else:
    print("The card number **** **** ** " +
          last.replace(", ", "") + " is not valid.")
