class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next
        
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            print("poof")
            return

        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node
    
    def __str__(self):
        output = ""
        
        current_node = self.head
        while current_node is not None:
            output += f" -> {current_node.data}"
            current_node = current_node.next
        
        return output
    
    def reverse(self):
        buffer = None
        new_head = None

        while self.head is not None:
            buffer = self.head.next
            self.head.next = new_head
            new_head = self.head
            self.head = buffer
        
        self.head = new_head

if __name__ == "__main__":
    ll = LinkedList()

    ll.append(3)
    ll.append(4)
    ll.append(5)

    print(ll)

    ll.reverse()

    print(ll)
