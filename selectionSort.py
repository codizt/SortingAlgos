def selectionSort():
    # Initialize variables
    unsortedList = [5, 3, 6, 2, 10]
    sortedList = []
    # Loop through the list
    for i in range(len(unsortedList)):
        # Find the smallest value in the unsorted list
        smallest = unsortedList[0]
        for j in range(len(unsortedList)):
            if unsortedList[j] < smallest:
                smallest = unsortedList[j]
        # Append the smallest value to the sorted list
        sortedList.append(smallest)
        # Remove the smallest value from the unsorted list
        unsortedList.remove(smallest)
    # Print the sorted list
    print(sortedList)