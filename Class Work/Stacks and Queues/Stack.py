class Stack:
    def __init__(self):
        self.__list = list()

    def push(self, data):
        self.__list.append(data)
    
    def peek(self):
        return self.__list[len(self.__list) - 1]
    
    def pop(self):
        return self.__list.pop()


if __name__ == "__main__":
    myStack = Stack()

    myStack.push(5)
    print(myStack.peek())
    myStack.push(6)
    print(myStack.peek())
    print(myStack.pop())
    print(myStack.peek())
    myStack.push(7)
    print(myStack.peek())    
