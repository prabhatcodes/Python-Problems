class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying
    storage"""
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue"""
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element from the front
           Raise Empty Exception if the Queue is empty"""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove & Return the first element of the queue(ie FIFO
           Raise Empty Exception if the queue is empty"""
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front]
        self._data = (self._front+1)%len(self._data)
        self._size-=1
        return answer