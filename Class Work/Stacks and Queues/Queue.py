class Queue:
    def __init__(self):
        self.__items = []
    
    def enqueue(self, item):
        self.__items.insert(0, item)
    
    def dequeu(self):
        print(self.__items)
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items) - 1]

class FancyQueue:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.__head = None
        self.__tail = None
    
    def enqueue(self, data):
        new_node = self.Node(data)

        if self.__tail is not None:
            self.__tail.next = new_node
        self.__tail = new_node

        if self.__head is None:
            self.__head = self.__tail
    
    def dequeue(self):
        if self.__tail is None:
            return 
        elif self.__head.next is None:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next
    
    def peek(self):
        return self.__head.data if self.__head is not None else None
        

if __name__ == "__main__":
    queue = Queue()

    # queue.enqueue(5)
    # print(queue.peek())
    # queue.enqueue(6)
    # queue.enqueue(7)
    # print(queue.peek())
    # print(queue.dequeu())
    # print(queue.peek())

    fancyQueue = FancyQueue()

    fancyQueue.enqueue(5)
    fancyQueue.enqueue(6)
    fancyQueue.enqueue(7)

    print(fancyQueue.peek())

    fancyQueue.dequeue()
    print(fancyQueue.peek())

    fancyQueue.dequeue()
    print(fancyQueue.peek())

    fancyQueue.dequeue()
    print(fancyQueue.peek())
