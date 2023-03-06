'''This program takes caffeine amount
in an 8oz cup of coffee and returns
caffeine content and number of hours
based on circumstances listed
in the comments.'''

# -------------
# Camrie Campos
# CSIS-1300-01 Spring 2023
# January 30, 2023
# Coding Three Assignment
# Due February 7, 2023
# ------------------

# Initialize variables
INITIAL = 130
CAFFEINE = 0.13
newAmount = float(INITIAL)

# Ask user for name
name = input("\n\nPlease enter your name: ")

# Calculate how many hours it takes to
# have 65mg of caffeine remaining in system
numHours = 0

while newAmount > 65:
    percent = float(newAmount * CAFFEINE)
    newAmount = newAmount - percent
    numHours = numHours + 1

# Share the number of hours with the user
print(name + " has less than 65mg of caffeine " +
      "in their system at", numHours, "hours " +
      "after one cup of coffee.")


# Calculate the amount of caffeine in
# the system after 24 hours
newAmount = float(INITIAL)
for i in range(24):
    percent = float(newAmount * CAFFEINE)
    newAmount = newAmount - percent

# Share caffeine content after 24 hours with user
print(name + " has", round(newAmount, 2), "mg of caffeine in " +
      "their system after 24 hours with one cup of coffee.")


# Initialize new variables to find how much
# caffeine remains after drinking a cup of
# coffee each hour for 24 hours
COFFEE = INITIAL * 24

# Calculate the amount of caffeine after
# 24 cups of coffee in 24 hours
newAmount = float(COFFEE)
for i in range(24):
    percent = float(newAmount * CAFFEINE)
    newAmount = newAmount - percent

# Share previous calculation with user
print(name + " has", round(newAmount, 2), "mg of caffeine in " +
      "their system after 24 hours of drinking a cup of " +
      "coffee each hour.")


# CREATIVE ELEMENT
# Print out the healthy amount of coffee per day (personalized)
print("\nHealthy adults shouldn't have more than 400 mg of caffeine a day.")
print("Drinking about 3 8-oz cups of coffee a day will help", name, "stay healthy.")


# THOUGHTS
# -------------------
# This program was a little tricky. I'd had some trouble getting the
# loops to run without creating infinite loops or incorrect calculations.
# I do hope there can be some more flexibility in the instructions for
# future programming assignments - I personally like including the user
# a bit more in my programs, so having assignments that provide that
# outlet for me would be appreciated.
# -------------------
