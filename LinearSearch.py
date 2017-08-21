# Linear Search algorithm to loop through a list

def LinearSerach(myList, myItem):
    position = 0
    found = False

    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
        position += 1

    return found, position


if __name__ == "__main__":
    Yourlist = [1, 5, 7, 6, 8, 9, 4, 3, 0, 20, 10]
    item = input("Enter the number to be searched! ")
    itemFound, Position = LinearSerach(Yourlist, item)

    if itemFound:
        print("Number exists at position %d" % Position)
    else:
        newItem = raw_input("Number does not exist, Do You want to add it to the list? y/n: ")
        if newItem == "y":
            Yourlist.append(item)
            print("Number has been added to list!")
            for x in Yourlist:
                print(x)
        else:
            print("Thank you, process stopped")
