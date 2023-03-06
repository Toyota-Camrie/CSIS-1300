'''A program that provides information
on the height of a ball thrown
straight up into the air'''

# ----------------------------------------
# Camrie Campos
# February 10, 2023
# CSIS 1300
# Spring 2023
# Due March 7, 2023
# ----------------------------------------

# ----------------------------------------
# Start of main


def main():

    # Call getInput
    # and set return values
    # to tuple variable

    initials = getInput()

    # Call maxHeight function
    # and initialize value
    maximum = maxHeight(initials[0], initials[1])

    # Call exFinal function
    # and set value to a
    # variable
    xfine = exFinal(initials[0], initials[1])

    # Call exDistance function
    # and set value to variable
    distance = exDistance(initials[1])

    # Print out results on
    # separate lines
    print("\n\nThe maximum height of the ball is", maximum, "feet.")
    print("The amount of time it takes the ball to return to the",
          "ground is", round(xfine, 2), "seconds.")
    print("The distance in the x-direction using the initial",
          "height and velocity is", distance, "meters.\n\n")

# End of main---------------------------------


'''A function called getInput
that gets the height and velocity
from user'''
def getInput():

    # Ask user for height in feet
    # and initial velocity in feet
    # per second
    height = input("\nEnter the height in feet: ")
    velocity = input("Enter the velocity in feet per second: ")

    # Call isValid function to verify
    # input is correct data type
    if isValid(height, velocity):
        return height, velocity
    print("Input is not valid.")

# End of getInput()----------------------------------


'''A function called isValid
to verify data type of
height and velocity are correct'''
def isValid(h, v):

    # Check input from user
    # height and then velocity
    if h.isdigit() and v.isdigit():
        return True

    # return False otherwise
    return False

# End of isValid()----------------------------------


'''A function called maxHeight
to calculate the maximum height
of the ball'''
def maxHeight(h, v):

    # Set variables equal to integers
    h = int(h)
    v = int(v)

    # Use equation v/32
    # to set the maximum height
    # to max variable
    time = v / 32
    maxh = h + (v * time) - (16 * (time ** 2))

    # Round the answer to 2 decimal places
    maxh = round(maxh, 2)

    # Return max height
    return maxh

# End of maxHeight()----------------------


'''A function called exFinal
to find out when the ball is
at the ground again'''
def exFinal(h, v):

    # Initialize time variable
    # and make parameters integers
    time = 0
    h = int(h)
    v = int(v)

    # Use equation
    # h + vt - 16(t^2)
    # to find when the ball hits
    # the ground
    while h >= 0:
        h = h + (v * time) - (16 * (time ** 2))
        time += 0.1

    # Round answer to 2 decimal places
    time = round(time, 2)

    # Return the time found
    return time

# End of exFinal()------------------------------------------

# ----------------------------------------
# CREATIVE ELEMENT - new function
# Also use kinematic equations
# for if the ball had been
# launched in a horizontal
# direction from a height h

# Use the initial inputs to
# calculate the total distance
# traveled in the x-direction
# ----------------------------------------

'''A function exDistance
calculates the total distance
traveled in the x-direction'''
def exDistance(v):

    # Make parameter an integer
    v = int(v)

    # Convert velocity
    # into meters per second
    v = (v * 12 * 2.54) / 100

    # Ask user for time
    time = int(input("Enter a time: "))

    # Use the time to calculate
    # the total distance in
    # the x-direction using
    # xf = xi + vi(t)
    final = 0 + v * time

    # Round final answer to 2 decimal places
    final = round(final, 2)

    # Return final value to user
    return final

# End of exDistance()------------------------


# Call main function
main()

# -----------------------------------
# THOUGHTS
# This program was pretty fun. I don't
# usually have many opportunities to practice
# physics outside of my current physics class,
# so the extra practice was appreciated to
# further my understanding in two classes,
# in this case.
# -----------------------------------
