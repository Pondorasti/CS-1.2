class DoubleLinkedList:

    class Node:
        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.previous = previous

        def __str__(self):
            return self.data
    
    def __init__(self, *args):
        self.head = None

        for data in args:
            self.append(data)
    
    def append(self, data):
        node = self.head

        if node is None:
            self.head = self.Node(data)
            return
        
        while node.next is not None:
            node = node.next
        
        new_node = self.Node(data, previous=node)
        node.next = new_node
    
    def prepend(self, data):
        pass

    def __str__(self):
        result = ""

        node = self.head
        while node is not None:
            result += f"Data: {node.data}, Previous: {node.previous}, Next: {node.next}\n"
            node = node.next
        
        return result


if __name__ == "__main__":
    dll_songs = DoubleLinkedList("Sunny", "Cloudy")

    dll_songs.append("Alex")
    dll_songs.append("Tian")
    dll_songs.append("Rafa")
    dll_songs.append("Sam")

    print(dll_songs)
