def BubbleSort(myList):
    moreSwaps = True  # initiate more swaps as true
    while moreSwaps:
        moreSwaps = False  # Jump out of while loop
        for element in range(len(myList) - 1):  # Swapping Loop
            if myList[element] > myList[element + 1]:
                moreSwaps = True
                temp = myList[element]
                myList[element] = myList[element + 1]
                myList[element + 1] = temp
    return myList  # sorted list returned

# Function to test bubble sort
def TestBubbleSort():
    newList = [4, 7, 9, 7, 5, 12, 98, 34, 0, 1]
    sortedList = BubbleSort(newList)
    print(sortedList)


TestBubbleSort()
