class Stack:
    def __init__(self):
        self.__list = list()

    def push(self, data):
        self.__list.append(data)
    
    def peek(self):
        return self.__list[len(self.__list) - 1]
    
    def pop(self):
        return self.__list.pop()
    
    def isEmpty(self):
        return False if self.peek() is None else True

def reverse_num(num):
    stack = Stack()
    
    while num >= 1:
        stack.push(num % 10)
        num = int(num / 10)
    
    while stack.isEmpty() is True:
        print(stack.pop())
        # num = num * 10 + stack.pop()

if __name__ == "__main__":
    number = 123
    reverse_num(number)
    # print(number)
