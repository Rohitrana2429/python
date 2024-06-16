def newSwap(newList):
    # Determine the size of the list
    size = len(newList)
    
    # Swap the first and last elements
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    
    return newList

# Define the list outside the function call
myList = [12, 34, 35, 54, 5, 65]

# Call the function and print the result
print(newSwap(myList))
