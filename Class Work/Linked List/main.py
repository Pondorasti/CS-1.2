from LinkedList import LinkedList

linked_list = LinkedList()
linked_list.prepend("odin")
linked_list.prepend("alex")

linked_list.pop_at_index(0)
print(linked_list)

linked_list.prepend("jess")



linked_list.append("yin")
linked_list.prepend("starlight")
# linked_list.print()
print(linked_list)


linked_list.pop_head()
print(linked_list)


linked_list.pop_at_index(2)
print(linked_list)
