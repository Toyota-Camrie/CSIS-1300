'''This program reads in a file of numbers and
1. Displays the number of numbers in the file,
2. Displays the largest number in the file, and
3. Displays the smallest number in the file.'''

# Camrie Campos
# CSIS-1300-01
# Spring 2023
# Coding 7
# Due March 23

# CREATIVE ELEMENT
# --------------------------------
# Organize numbers by smallest to
# largest in a function called
# sortNumbersInFile
# --------------------------------


# Start of main
def main():
    '''Main function to call getData,
    call getNumber, call getLargest,
    call getSmallest, and call
    sortNumbersInFile
    functions and return the results.'''

    # Create list to store data from
    # getData function
    listNumbers = getData()

    # Call getNumber function
    # with listNumbers as parameter
    print("The total number of numbers",
          "in the file is", getNumber(listNumbers))

    # Call getLargest function
    # with listNumbers as parameter
    print("The largest number in the file is",
          getLargest(listNumbers))

    # Call getSmallest function
    # with listNumbers as parameter
    print("The smallest number from the file",
          "is", getSmallest(listNumbers))

    # Create new list to take sorted
    # numbers from sortNumbersInFile
    # function
    sortedList = sortNumbersInFile(listNumbers)
    print("\nThe sorted file is: \n")
    for line in sortedList:
        print(line)


# End of main --------------------


# Start of getData function
def getData():
    '''getData function
    takes no parameters and
    returns a list of the
    data in the file'''

    # Open the file Numbers.txt
    openFile = open(r"C:\Users\camri\hello\Coding7\Numbers-1.txt", 'r')

    # Create a list of the data stored
    # in the file
    numbersList = [line.rstrip() for line in
                   openFile]

    # Close the file
    openFile.close()

    # Return the list of data
    return numbersList

# End of getData function ---------


# Start of getNumber function
def getNumber(listofNums):
    '''getNumber function
    takes list from getData and
    returns a number that is
    the total number of numbers
    in the file'''
    # Initialize integer to
    # be returned
    sum = 0

    # Use a for loop to add
    # the numbers from the list
    # together into integer
    for i in range(len(listofNums)):
        sum += 1

    # Return the sum
    return sum

# End of getNumber function ------


# Start of getLargest function
def getLargest(listofNums):
    '''getLargest function
    takes list from getData and
    returns the largest
    number in the file'''

    return max(listofNums)

# End of getLargest function -----


# Start of getSmallest function
def getSmallest(listofNums):
    '''getSmallest function
    takes list from getData and
    returns the smallest
    number in the file'''

    return min(listofNums)

# End of getSmallest function ----


# Start of sortNumbersInFile funciton
def sortNumbersInFile(listofNums):
    '''sortNumbersInFile function
    takes list from getData and
    return list of sorted
    numbers by smallest to largest'''

    # Create a string with the
    # values from the list
    # without the newline characters
    numbers = ""

    numbers = numbers.join(listofNums)

    # Create a new list that
    # has the values from the
    # previously-created string
    sortedNumbers = sorted(numbers)

    # Return the newly sorted list
    return sortedNumbers

# End of sortNumbersInFile function


# Call main function
main()


# THOUGHTS
# --------------------------------
# Add thoughts here
# --------------------------------
