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

# adding element at an arbitrary position
linked_lst.insert(1, 'Unknown Planet')

print("All Elements of Linked List are :")
print(linked_lst)

# deleting the last element
linked_lst.pop()

print("elements in the linked_list:")
print(linked_lst)

# removing a specific element
linked_lst.remove('fourth')

print("elements in the linked_list:")
print(linked_lst)

