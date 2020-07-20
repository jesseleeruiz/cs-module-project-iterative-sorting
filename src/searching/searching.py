def linear_search(arr, target):
    for number in arr:
        if target == number:
            return arr.index(number)
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    arr_length = len(arr)
    while arr_length > 0:
        for number in arr:
            if target == number:
                return arr.index(number)
        arr_length /= 2
    return -1  # not found
