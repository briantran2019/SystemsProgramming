def binary_search(array, val):
    left = 0
    right = len(array) - 1
    middle = left + (right - left)//2
    while (left <= right):
        middle = left + (right - left)//2
        if array[middle] == val:
            return middle
        elif array[middle] > val:
            right = middle - 1
        elif array[middle] < val:
            left = middle + 1
        else:
            return -1

arr = [n for n in range(10)]
print(binary_search(arr, 3))
print(binary_search(arr, 7))
print(binary_search(arr, 11))
print(binary_search(arr, 20))