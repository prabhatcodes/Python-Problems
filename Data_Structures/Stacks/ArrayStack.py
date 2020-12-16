class Empty(Exception):
    """Error attempting to access an element from an empty container.
    I.E. when the stack is empty"""
    pass

class ArrayStack:

    def __init__(self):
        """LIFO stack implementation using a list as the base data structure"""
        self._data = [] # non public instance

    def __len__(self):
        """Returns the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Add element to the top of the stack"""
        self._data.append(e) # Adds an element at the end of the list.

    def top(self):
        """Returns the element at the top without removing it
           Raise Empty Exception in case the Stack is empty"""
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._data[-1] # Reads the element at the end of the list

    def pop(self):
        """Returns and Removes the element at the top of the stack
           Raise Empty Exception if stack is empty"""
        if self.is_empty():
            raise Empty("Stack is Empty")
        self._data.pop() # Last item removed from end of list