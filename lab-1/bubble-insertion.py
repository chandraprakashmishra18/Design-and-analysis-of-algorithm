def compare_bubble_insertion(random_data, sorted_data, reverse_data):
  def bubble(data):
    arr=data.copy()
    comparisons=0
    swaps=0
    n=len(arr)
    for i in range(n):
      swapped=False
      for j in range(n-i-1):
        comparisons+=1
        if arr[j]>arr[j+1]:
          arr[j],arr[j+1]=arr[j+1],arr[j]
          swaps+=1
          swapped=True
      if not swapped:
        break
    return arr, comparisons, swaps
    
  # Insertion Sort
  def insertion(data):
    arr=data.copy()
    comparisons=0
    shifts=0
    n=len(arr)
    for i in range(1,n):
      key=arr[i]
      j=i-1
      while j>=0:
        comparisons+=1
        if arr[j]>key:
          arr[j+1]=arr[j]
          shifts+=1
          j-=1
        else:
          break
      arr[j+1]=key
    return arr, comparisons, shifts

  # running the functions created 
  bubble_random=bubble(random_data)
  insertion_random=insertion(random_data)

  bubble_sorted=bubble(sorted_data)
  insertion_sorted=insertion(sorted_data)

  bubble_reverse=bubble(reverse_data)
  insertion_reverse=insertion(reverse_data)

  if bubble_random[1] < insertion_random[1]:
        better_random = "Bubble Sort"
  elif insertion_random[1] < bubble_random[1]:
        better_random = "Insertion Sort"
  else:
        better_random = "Both Equal"


  if bubble_sorted[1] < insertion_sorted[1]:
        better_sorted = "Bubble Sort"
  elif insertion_sorted[1] < bubble_sorted[1]:
        better_sorted = "Insertion Sort"
  else:
        better_sorted = "Both Equal"


  if bubble_reverse[1] < insertion_reverse[1]:
        better_reverse = "Bubble Sort"
  elif insertion_reverse[1] < bubble_reverse[1]:
        better_reverse = "Insertion Sort"
  else:
        better_reverse = "Both Equal"
  
  # Output array
  output=[
    "Sorting Performance Report",
    "Random Dataset",
    f"Bubble Sorted: {' '.join(map(str, bubble_random[0]))}",
    f"Bubble Comparisons: {bubble_random[1]}",
    f"Bubble Swaps: {bubble_random[2]}",
    f"Insertion Sorted: {' '.join(map(str, insertion_random[0]))}",
    f"Insertion Comparisons: {insertion_random[1]}",
    f"Insertion Shifts: {insertion_random[2]}",
    f"Better Algorithm: {better_random}",
    f"Sorted Dataset",
    f"Bubble Sorted: {' '.join(map(str, bubble_sorted[0]))}",
    f"Bubble Comparisons: {bubble_sorted[1]}",
    f"Bubble Swaps: {bubble_sorted[2]}",
    f"Insertion Sorted: {' '.join(map(str, insertion_sorted[0]))}",
    f"Insertion Comparisons: {insertion_sorted[1]}",
    f"Insertion Shifts: {insertion_sorted[2]}",
    f"Better Algorithm: {better_sorted}",
    "Reverse Dataset",
    f"Bubble Sorted: {' '.join(map(str, bubble_reverse[0]))}",
    f"Bubble Comparisons: {bubble_reverse[1]}",
    f"Bubble Swaps: {bubble_reverse[2]}",
    f"Insertion Sorted: {' '.join(map(str, insertion_reverse[0]))}",
    f"Insertion Comparisons: {insertion_reverse[1]}",
    f"Insertion Shifts: {insertion_reverse[2]}",
    f"Better Algorithm: {better_reverse}" 
  ]
    
  return output