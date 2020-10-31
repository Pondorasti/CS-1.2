class LinkedList:

    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add a new node to the end of the list."""
        node = self.head

        if node is None:
            self.head = self.Node(data)
            return 

        while node.next is not None:
            node = node.next
        node.next = self.Node(data)
    
    def prepend(self, data):
        """Add a new node to the start of the list."""
        self.head = self.Node(data, self.head)
    
    def print(self):
        """Print all the nodes in the list."""
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next



songs = LinkedList()

songs.append("Black Betty")
songs.append("Sweater Weather")
songs.prepend("Be happy")
songs.append("Sam")
songs.prepend("Rafa")

songs.print()