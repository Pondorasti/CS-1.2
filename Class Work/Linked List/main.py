from LinkedList import LinkedList

linked_list = LinkedList()
linked_list.prepend("odin")
linked_list.prepend("alex")

clone_linked_list = linked_list.clone()


linked_list.pop_head()
print(linked_list)
print(clone_linked_list)

# linked_list.prepend("jess")


# linked_list.append("yin")
# linked_list.prepend("starlight")
# print(linked_list)


# linked_list.pop_head()
# print(linked_list)


# linked_list.pop_at_index(2)
# print(linked_list)


# print(clone_linked_list)