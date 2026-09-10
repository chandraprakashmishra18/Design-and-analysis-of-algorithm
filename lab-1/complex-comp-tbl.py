def generate_runtime_complexity_table(n):

    linear_search = n
    binary_search = math.floor(math.log2(n)) + 1
    bubble_sort = n * (n - 1) // 2
    insertion_sort = n * (n - 1) // 2

    result = []

    print ("Runtime Complexity Comparison")
    print("Method ObservedCount ExpectedComplexity Observation")

    print(
        f"Linear Search {linear_search} O(n) "
        f"Grows linearly"
    )

    print(
        f"Binary Search {binary_search} O(log n) "
        f"Grows logarithmically"
    )

    print(
        f"Bubble Sort {bubble_sort} O(n^2) "
        f"Grows quadratically"
    )

    print(
        f"Insertion Sort {insertion_sort} O(n^2) "
        f"Grows quadratically"
    )

    return "\n".join(result)