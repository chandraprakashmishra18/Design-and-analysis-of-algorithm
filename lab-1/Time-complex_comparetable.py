from math import log2 , floor
def generate_runtime_complexity_table(n):
    # your code goes here
    output=[
      "Runtime Complexity Comparison",
      "Method ObservedCount ExpectedComplexity Observation",
      f"Linear Search {n} O(n) Grows linearly",
      f"Binary Search {floor(log2(n))+1} O(log n) Grows logarithmically",
      f"Bubble Sort {n*(n-1)//2} O(n^2) Grows quadratically",
      f"Insertion Sort {n*(n-1)//2} O(n^2) Grows quadratically"
    ]
    return output