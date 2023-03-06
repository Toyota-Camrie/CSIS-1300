"""This program calculates the number of cents from
user input in quarters, dimes, nickels, and pennies.
"""

# -------------------
# Camrie Campos
# CSIS-1300-01 Spring 2023
# January 12, 2023
# Coding Two Assignment
# Due January 31, 2023
# -------------------

# Initialize an integer variable to equal the number of cents given as input
n = int(input("Enter the number of cents: "))

# CREATIVE ELEMENT:
# --------------------
# if statement for numbers below 1
if n < 1:
    raise Exception("That is not a valid integer. Please try again.")
# --------------------

# if statement for numbers above 99
if n > 99:
    print("Please enter a number between 0 and 99.")


# Use if statement to determine any possible cent input with quarters, dimes, nickels, and pennies
if n <= 99 and n >= 25:

    # Calculate the number of quarters
    q = n // 25

    # Subtract the number of cents in quarters from the original number
    n = n - (25 * q)

    # if statement for if there are no cents left from the quarter calculation
    if n < 1:
        print("Your change is ", q, " quarter(s).")

    # elif statement for figuring out if there are any dimes, nickels, or pennies that can be found
    elif n >= 10:

        # Calculating the number of dimes
        dim = n // 10

        # Subtracting the cents in the number of dimes from the original amount
        n = n - (10 * dim)

        # if statement for no other coins besides quarters and dimes from the cent amount
        if n < 1:
            print("Your change is ", q, " quarter(s) and ", dim, " dime(s).")

        # elif statement for no nickels and only quarters, dimes, and pennies
        elif n < 5:
            print("Your change is ", q, " quarter(s), ",
                  dim, " dime(s), and ", n, " pennies.")

        # elif statement for quarters, dimes, nickels, and pennies
        elif n >= 5:

            # Variable for the number of pennies left over
            pen = n - 5
            print("Your change is ", q, " quarter(s), ", dim,
                  " dime(s), 1 nickel, and ", pen, "pennies.")

    # elif statement for quarters, nickels, and pennies (no dimes) possibility
    elif n > 5 and n < 10:
        pen = n - 5
        print("Your change is ", q, " quarter(s), 1 nickel, and ", pen, " pennies.")

    # elif statement for quarters and nickels (no dimes or pennies) possibility
    elif n == 5:
        print("Your change is ", q, " quarter(s) and 1 nickel.")

    # else statement for only other possibility (quarters and pennies)
    else:
        print("Your change is ", q, "quarter(s) and ", n, " pennies.")


# Use elif statement to determine if integer is less than 25 and
# greater than 10 (dimes, nickels, and pennies possible)
elif n < 25 and n > 10:

    # Calculating the number of dimes
    dim = n // 10

    # Subtracting the number of cents represented by dimes by original cent amount given by user
    n -= 10 * dim

    # if statement for dimes only possibility
    if n < 1:
        print("Your change is ", dim, " dime(s).")

    # elif statement for dimes, nickels, and pennies possibility
    elif n > 5:
        pen = n - 5
        print("Your change is ", dim, " dime(s), 1 nickel, and ", pen, " pennies.")

    # elif statement for dimes and nickels only possibility
    elif n == 5:
        print("Your change is ", dim, " dime(s) and 1 nickel.")

    # else statement for dimes and pennies only possibility
    else:
        print("Your change is ", dim, " dime(s) and ", n, " pennies.")


# Use elif statement to determine if integer is less than 10 and greater than 5
# (1 nickel and maybe some pennies)
elif n < 10 and n > 5:
    pen = n - 5
    print("Your change is 1 nickel and ", n, " pennies.")


# Use elif statement to determine if the integer is less than 5 (only pennies)
elif n < 5:
    print("Your change is ", n, " pennies.")
