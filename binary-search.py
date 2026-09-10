def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [2, 4, 6, 8, 10, 12]
print(binary_search(arr, 10))


# Time: Best O(1), Average/Worst O(log n)
# Space: O(1)