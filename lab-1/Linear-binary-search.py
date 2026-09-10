def compare_search_algorithms(arr, target):
  # Binary Search 
    def binary_search(arr,target):
        low=0
        high=len(arr)-1
        comparisons=0
        result_index=-1
      
        while low<=high:
            mid=(low+high)//2
            comparisons+=1
            if arr[mid]==target:
                result_index = mid   
                high = mid - 1 
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1
        
        return result_index, comparisons

    # Linear Search
    def linear_search(arr,target):
        comparisons=0
        for i in range(len(arr)):
            comparisons+=1
            if arr[i]==target:
                return i,comparisons
        return -1,comparisons

    lin_index, lin_comp = linear_search(arr, target)
    bin_index, bin_comp = binary_search(arr, target)

    result = [
        "Search Comparison Report",
        "Linear Search",
        f"Index: {lin_index}",
        f"Comparisons: {lin_comp}",
        "Binary Search",
        f"Index: {bin_index}",
        f"Comparisons: {bin_comp}",
    ]


    if lin_comp < bin_comp:
        result.append("Better Algorithm: Linear Search")
    elif bin_comp < lin_comp:
        result.append("Better Algorithm: Binary Search")
    else:
        result.append("Better Algorithm: Both Equal")

    return result