# Using a linked list in Python

# Referred to this: https://www.openbookproject.net/thinkcs/python/english2e/ch18.html

# We have seen examples of attributes that refer to other objects, which are called embedded references.
# A common data structure, the linked list, takes advantage of this feature.

# Linked lists are made up of nodes, where each node contains a reference to the next node in the list.
# In addition, each node contains a unit of data called cargo/value.

# A linked list is considered a recursive data structure because it has a recursive definition.

# A linked list is either:

    # 1. An empty list, represented by None,
    # 2. A node that contains a cargo/value object and a reference to a linked list.

class Node:
    def __init__(self,  cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __repr__(self):
        

    def __str__(self):
        return(self.cargo)
        
