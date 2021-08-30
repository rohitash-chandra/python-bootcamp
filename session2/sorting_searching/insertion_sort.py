# Python program for implementation of Insertion Sort
#https://www.geeksforgeeks.org/insertion-sort/

#https://en.wikipedia.org/wiki/Insertion_sort

# Function to do insertion sort
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
 
# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
 
# This code is contributed by Mohit Kumra


# Exercise. Implement bubble sort and insertion sort as functions. for large list of values in range [0-100], eg. 1000, 2000, 3000, 4000
#report the time and compare both functions. Run 30 experiments for each case. 

# Further exercise - study merge and quicksort and compare them with above.



