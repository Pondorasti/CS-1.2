class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, tuple):
    new_node = Node(tuple)

    if self.head is None:
      self.head = new_node
      self.tail = self.head
    else:
      self.tail.next = new_node
      self.tail = self.tail.next

  def find(self, key):
    node = self.head
    while node is not None:
      if node.data[0] == key:
        return node.data[1]
      
      node = node.next

  def __str__(self):
    output = ""
    node = self.head
    while node is not None:
      output += f" -> [{node.data}]"
      node = node.next  
    
    return output


if __name__ == "__main__":
  ll = LinkedList()
  ll.append(("Alex", 18))
  print(ll)

  ll.append(("Jess", 30))
  print(ll)

  ll.append(("Alex", 21))
  print(ll)

  print(ll.find('Jess'))