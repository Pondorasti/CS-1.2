a = [1, 2, 3, 5, 6]
def recursive_search(array, item_to_find, current_index=0):
    if current_index == len(array):
        return None
    elif array[current_index] == item_to_find:
        return current_index
    else:
        return recursive_search(array, item_to_find, current_index + 1)

# print(recursive_search(a, 3))



def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while (start <= end):
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return None


a = [3,4,5,6,10,12,20]
print(binary_search(a, 5))