import random


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = random.choice(range(len(arr)))
    pivot = arr[pivot_index]

    left = []
    right = []
    for item in arr:
        if pivot > item:
            left.append(item)
        else:
            right.append(item)

    return quicksort(left) + quicksort(right)


arr = [9, 2, 5, 6, 4, 3, 7, 10, 1, 12, 8, 11]
print(quicksort(arr))


# def improvedQuicksort(arr):
#   if len(arr) <= 1:
#         return arr

#   pivot_index = random.choice(range(len(arr)))
#   pivot = arr[pivot_index]

#   left_pointer = 0
#   right_pointer = len(arr) - 1

#   while left_pointer < right_pointer:
#       while left_pointer < len(arr) and arr[left_pointer] > pivot:
#         left_pointer += 1
#       while right_pointer >= 0 and pivot < arr[right_pointer]:
#         right_pointer -= 1
      
#   for item in arr:
#       if pivot > item:
#           left.append(item)
#       else:
#           right.append(item)
  
#   return quicksort(left) + quicksort(right)
