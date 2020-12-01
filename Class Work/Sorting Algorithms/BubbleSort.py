arr = [4, 1, 2, 0, 7, 6]

def bubbleSort(arr):

  sorted = False
  while not sorted:
    sorted = True
    for index in range(0, len(arr) - 1):
      if arr[index] > arr[index + 1]:
        (arr[index], arr[index + 1]) = (arr[index + 1], arr[index])
        sorted = False

print(arr)
bubbleSort(arr)
print(arr)



