# Linked List

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None # Null

class LinkedList:

    def __init__(self):
        self.head = None

if __name__=="__main__":

        llist = LinkedList()

        llist.head = Node(1)
        second = Node(2)
        third = Node(3)

        llist.head.next = second # link first node with second
        second.next = third # Link second node with the third node

# Linked List traversal

def __init__(self):
    temp = self.head
    while (temp):
        print (temp.data)
        temp = temp.next