# Binary Search Algorithm

# Define a function that takes in a sorted list and item we shall be looking for
def BinarySearch(sortedList, item):
    found = False  # boolean to represent whether item has been found
    bottom = 0  # define Bottom of the list index position
    top = len(sortedList) - 1  # define top of the list index position
    loop = 0
    # Loop until item is found and bottom index is less than top return found
    while bottom <= top and not found:
        middle = (top + bottom) // 2  # Get the middle index
        if sortedList[middle] == item:
            found = True
        elif sortedList[middle] > item:  # if item is less than middle
            top = middle - 1
        else:
            bottom = middle + 1  # if item is greater than middle
        loop += 1
    return found, loop


# Run main function
if __name__ == "__main__":
    Yourlist = [1, 2, 3, 6, 8, 9, 10, 34, 90, 99, 400]  # Sorted list
    target = int(input("Enter the number to be searched! "))
    targetFound, counter = BinarySearch(Yourlist, target)  # Call BinarySearch function

    if targetFound:
        print("Number exists after looping %d" % counter + " time(s)")
    else:
        print ("Number does not exist")
