def merge_sort(arr):
  if len(arr) <= 2:
    return sorted(arr)
  
  mid = len(arr) // 2
  left_list = arr[:mid]
  right_list = arr[mid:]

  return merge(merge_sort(left_list), merge_sort(right_list))


def merge(left_list, right_list):
  left_index = 0
  right_index = 0

  left_len = len(left_list)
  right_len = len(right_list)

  new_list = []

  while left_index < left_len and right_index < right_len:
    if left_list[left_index] < right_list[right_index]:
      new_list.append(left_list[left_index])
      left_index += 1
    elif left_list[left_index] >= right_list[right_index]:
      new_list.append(right_list[right_index])
      right_index += 1

  # add leftover
  new_list += right_list[right_index:]
  new_list += left_list[left_index:]
  
  return new_list


# left = [3, 5]
# right = [3, 9, 12, 26, 92]

# print(right[:2])
# print(right[2:])

# print(merge(left, right))

arr = [-25, 104, 12, 3, 6, 9, 25, -25, 13, -13]
arr2 = [5, 10, -3, -10, 1, 100, 99]
print(merge_sort(arr2))