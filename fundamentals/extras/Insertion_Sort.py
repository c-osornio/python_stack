arr = [1, 5, 3, 2, 0, 8]


def insertionSort(arr):
    for i in range(1 , len(arr)):  # traverse through the entire array, starting at the second element so that we can manipulate the previous element
        runner = arr[i] #  set runner to hold the value of each element of the array starting at the second element
        j = i - 1  # set j to be the previous element's index from the runner
        while j >= 0 and runner < arr[j]: # while there is a previous element and runner is less than the previous element
            arr[j + 1] = arr[j] # swap elements, move the larger element to the right, dont use runner use arr[j+1] since we dont want the value of runner to change but we do want the array to change
            j -= 1 # now subtract 1 from j so we can compare elements until at the start of the array to break while loop or the runner larger than the previous element 
        arr[j+1] = runner # insert the runner value to where it is larger than the previous element
    return arr

print(insertionSort(arr))
