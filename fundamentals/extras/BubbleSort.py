arr = [1,5,3,2,0,8]*10

def bubbleSort(arr):
    count = 0
    for j in range(len(arr) -1):
        # print("\n\n", "-"*50, "Iteration", j)
        for i in range(len(arr)-1-j):
            count += 1
            # print("\n", "*"*80, "\nindex:", i, "value:", arr[i])
            # print("\n", "*"*80, "\ncomparing:", arr[i], "with:", arr[i+1])
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # print("swapped", arr[i], "and", arr[i+1])
                # print("array is now", arr)
            # else: 
                # print("No need to swap.", arr[i], "and", arr[i+1])
                # print("array is now", arr)
    print("# of evaluations", count)
    return arr

print(bubbleSort(arr))

def bubbleSort(arr):
    for j in range(len(arr) -1):
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr