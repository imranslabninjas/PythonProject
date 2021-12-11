# importing module
import collections

# initialising a deque() of arbitrary length
linked_lst = collections.deque()

# filling deque() with elements
linked_lst.append('Mercury')
linked_lst.append('Venus')
linked_lst.append('Earth')
linked_lst.append('Mars')
linked_lst.append('Jupiter')
linked_lst.append('Saturn')
linked_lst.append('Neptune')
linked_lst.append('Pluto')

print("All Elements of Linked List are :")
print(linked_lst)

# add element in arbitrary index
linked_lst.insert(1, 'Unknown Planet')

# ei link list er shob elements
print("All Elements of Linked List are")
print(linked_lst)

# last element pop kora
linked_lst.pop()

print("elements in the linked_list:")
print(linked_lst)

# ekta specific element remove kora
linked_lst.remove('fourth')

# ekhn linked list er bhitor ja ja ache
print("elements in the linked_list")
print(linked_lst)

