class LinkedList:
  class Node:
    def __init__(self, data):
      self.data = data
      self.next = None

  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, data):
    new_node = self.Node(data)
    if self.tail is not None:
      self.tail.next = new_node
    self.tail = new_node
    
    if self.head is None:
      self.head = new_node
  
  def prepend(self, data):
    new_node = self.Node(data)
    new_node.next = self.head
    self.head = new_node
    
    if self.tail is None:
      self.tail = new_node
  
  def pop_head(self):
    self.head = self.head.next
  
  # def pop_tail(self):
  #   self.tail = self.head.next

  def pop_at_index(self, index_to_pop):
    current_node = self.head
    current_index = 0

    
    if index_to_pop == current_index:
      self.head = None
      return

    while current_node is not None:
      if current_index + 1 == index_to_pop:
        current_node.next = current_node.next.next
        return
      
      current_node = current_node.next
      current_index += 1


  
  def __str__(self):
    answer = ""

    current_node = self.head
    while current_node is not None:
      answer += f"{current_node.data}\n"
      current_node = current_node.next 

    return answer
    