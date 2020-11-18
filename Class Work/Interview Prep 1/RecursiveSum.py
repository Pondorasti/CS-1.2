def sum_num(arr, sum=0, index=0):
    if index > len(arr) - 1:
        return sum
    else:
        return sum_num(arr, sum + arr[index], index + 1)

if __name__ == "__main__":
    print(sum_num([5, 4, 1]))
    print(sum_num([]))
