def linear_search(arr, target):
    # Your code here
    length = len(arr)
    tracker = 0
    if length > 1:
        while tracker < length:
            if arr[tracker] == target:
                return tracker
            else:
                tracker += 1
                continue

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = round((low+high)/2)
        if target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1
        else:
            return middle
    return -1  # not found
