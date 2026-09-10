from math import log2, floor
def generate_runtime_chart_report(sizes):
    # your code goes here
    output=[
      "Runtime Comparison Chart Data",
      "InputSize LinearSearch BinarySearch BubbleSort InsertionSort"
    ]

    for n in sizes:
      ls=n
      bs=floor(log2(n))+1
      bub=n*(n-1)//2
      ins=n*(n-1)//2
      row=f"{n} {ls} {bs} {bub} {ins}"
      output.append(row)

    output_summary=[
      "Scalability Summary",
      "Algorithm Complexity Scalability",
      "Linear Search O(n) Moderate",
      "Binary Search O(log n) Excellent",
      "Bubble Sort O(n^2) Poor",
      "Insertion Sort O(n^2) Poor",
      "Key Observations",
      "Best Algorithm: Binary Search",
      "Most Expensive Algorithm: Bubble Sort",
      "Conclusion: Logarithmic algorithms scale better for large inputs"
    ]
  
    return output+output_summary