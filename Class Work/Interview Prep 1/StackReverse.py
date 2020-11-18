def reverse_num(num):
    stack = 0
    
    while num >= 1:
        stack = stack * 10 + num % 10
        num = int(num / 10)
    
    return stack

if __name__ == "__main__":
    number = 123
    print(reverse_num(number))
