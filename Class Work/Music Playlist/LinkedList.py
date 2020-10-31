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
    
    def delete_head(self):
        """Removes the first node in the list"""
        if self.head is not None:
            self.head = self.head.next
    
    def delete_tail(self):
        """Removes the last node in the list"""
        node = self.head

        if node is None:
            return 
        if node.next is None:
            self.head = None
            return
        
        while node.next.next is not None:
            node = node.next
        node.next = None

    
    def find(self, data):
        """find() -> bool"""
        node = self.head

        while node is not None:
            if node.data == data:
                return True
            
            node = node.next
        
        return False
    
    def delete(self, data): 
        """Delete the first occurence of data"""
        node = self.head

        if node is None:
            return 
        if node.data == data:
            self.delete_head()
            return 
        if node.next is None:
            return 

        while node.next is not None:
            if node.next.data == data:
                if node.next is None:
                    self.delete_tail()
                    return
                
                node.next = node.next.next 
                return

            node = node.next

    def reverse(self):        
        old_head = self.head
        new_head = None
        buffer_node = None
        while old_head is not None:
            # V1
            # new_head = self.Node(old_head.data, new_head)
            # old_head = old_head.next

            # V2
            buffer_node = old_head.next
            old_head.next = new_head
            new_head = old_head
            old_head = buffer_node
        
        self.head = new_head
            

if __name__ == "__main__":
    songs = LinkedList()

    songs.append("Black Betty")
    songs.append("Sweater Weather")
    songs.prepend("Be happy")
    songs.append("Sam")
    songs.prepend("Rafa")

    # songs.delete_head()
    # songs.delete_tail()
    # songs.delete_tail()

    # songs.delete_tail()
    # songs.delete_tail()
    # songs.delete_tail()

    # print(songs.find("Be Happy"))

    # songs.delete("Sam")

    songs.reverse()
    songs.print()