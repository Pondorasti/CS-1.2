arr = [4, 1, 2, 0, 7, 6]

def selectionSort(arr):
  for i in range(len(arr)):
    minIndex=i
    for j in range(i, len(arr)):
      if arr[minIndex] > arr[j]:
        minIndex = j

    (arr[i], arr[minIndex]) = (arr[minIndex], arr[i])


print(arr)
selectionSort(arr)
print(arr)