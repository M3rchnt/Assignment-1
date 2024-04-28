
# Function to sort a list via Bubble Sort Method
# Function sorts by starting from the first integer and moving it rightwards along the list until it is in its proper place 
def bubble_sort(unsorted, size):
    assert isinstance(unsorted, list) # Check to see if input is a list
    assert len(unsorted) == size # Check to see if list length is equal to defined fixed size
    for i in range(0, size, 1):
        assert unsorted[i] != None # Check to ensure list values are not None
        assert isinstance(unsorted[i], int) # Check to ensure list values are integers

    spare = 0 # Initialize a spare variable used in swapping numbers in list
    i = 0 
    while (i < len(unsorted)-1): 
        if unsorted[i] > unsorted[i+1]:
            index = i # Initialize index to start at the position the wrong value is at
            while (index+1 < len(unsorted)) and (unsorted[index] > unsorted[index+1]):
                spare = unsorted[index+1] # Swapping neighbouring numbers
                unsorted[index+1] = unsorted[index]
                unsorted[index] = spare
                index += 1
            if (i == 0): # Exception case for when the 0th index is the wrong value
                i -= 1
            else: # Every other exception case
                i -= 2
        i += 1
    return unsorted

fixed_size = 10 # Define fixed length
unsorted = [0] * fixed_size # Initialize list with fixed amount of entries
for i in range(fixed_size):
    unsorted[i] = 10-i # Fill list
print(f"Unsorted List Contents: {unsorted}")
sorted = bubble_sort(unsorted, fixed_size)
print(f"Sorted List Contents: {sorted}")