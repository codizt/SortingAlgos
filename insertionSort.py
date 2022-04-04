def insertionSort():
    # Get the input
    input = input("Enter a list of numbers separated by spaces: ")
    # Split the input into a list
    input = input.split()
    # Convert the list to integers
    input = [int(i) for i in input]
    # Sort the list
    for i in range(1, len(input)):
        j = i
        while j > 0 and input[j] < input[j-1]:
            input[j], input[j-1] = input[j-1], input[j]
            j -= 1
    # Print the sorted list
    print(input)