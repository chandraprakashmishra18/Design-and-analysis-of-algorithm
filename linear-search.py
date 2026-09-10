def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


arr = [5, 2, 8, 1, 9]
print(linear_search(arr, 8))

# Time: Best O(1), Average/Worst O(n)
# Space: O(1)