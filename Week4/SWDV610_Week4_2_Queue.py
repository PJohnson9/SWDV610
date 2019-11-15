# Patrick Johnson        11/14/2019 #
# SWDV 610 3W 19/FA2    Week 4 - #2 #
#####################################
# 2. Implement a queue using linked lists

class Queue:
    """ ADT Queue implemented in Python using a Linked List

    Intrinsic Methods:
        enqueue(element) - Adds reference to element to the end of the queue
        dequeue() - Removes and returns the reference at the front of the queue
                    Raises an error if queue has no elements
                
    Additional Methods:
        first() - Returns the reference to the element at the front of the queue
        last() - Returns the reference to the element at the end of the queue
        is_empty() - Returns True if the queue contains no elements
    """
    class _node:
        def __init__(self, data, next_node):
            self._data = data
            self._next = next_node
    
    class EmptyQueueException(Exception):
         def __init__(self):
             super().__init__("Queue has no elements.")
    
    def __init__(self):
        self._front = None
        self._end = None
        self._count = 0
        
    def __len__(self):
        return self._count
    
    def __str__(self):
        string = "{ "
        node = self._front
        while node != None:
            string += "{" + repr(node._data) + "} "
            node = node._next
        string += "}"
        return string
    
    def __repr__(self):
        return "Queue: " + self.__str__()
        
    def is_empty(self):
        return self._front == None
        
    def enqueue(self, data):
        if self._front == None:                 # Check if Queue is empty
            self._end = self._node(data, None)  # New element goes at end
            self._front = self._end             # front is same as end
        else:                                        # Queue is not empty
            self._end._next = self._node(data, None) # Create new node after end
            self._end = self._end._next              # Update end to point to new node
        self._count += 1
        
    def dequeue(self):
        if self._front == None:
            raise self.EmptyQueueException
        else:
            dequeued_node = self._front        # Get node at front of queue
            self._front = dequeued_node._next  # Set next node as new front
            if self._front == None:     # Check if queue is empty
                self._end = None        # Remove _end reference if queue is empty
            self._count -= 1
            return dequeued_node._data

    def first(self):
        if self._front == None:
            raise self.EmptyQueueException
        else:
            return self._front._data
        
    def last(self):
        if self._end == None:
            raise self.EmptyQueueException
        else:
            return self._end._data
        
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1); q.enqueue(2); q.enqueue(3);  q.enqueue(4); q.enqueue('5')
    print("Queue:",q)
    print("First:",q.first())
    while not q.is_empty():
        print("Dequeue:",q.dequeue())