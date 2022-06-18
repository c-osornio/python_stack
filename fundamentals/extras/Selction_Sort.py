arr = [1,5,3,2,0,8]

def selectionSort(arr):
    for i in range(len(arr)):   # traverse through the entire array
        indexMin = i   # find minimum element in remaining unsorted array, marker for the minimum's index
        for j in range(i + 1, len(arr)): # traverse through the remaining unsorted array, starting at the 2nd element then to the end of the array
            if arr[indexMin] > arr[j]: # starting at the 1st element, compare value to the next element
                indexMin = j    # if the next element is lower than the current element
                arr[i], arr[indexMin] = arr[indexMin], arr[i] # swap the elements so that the min is moved to the start of the remainin UNSORTED array
    return arr


print(selectionSort(arr))