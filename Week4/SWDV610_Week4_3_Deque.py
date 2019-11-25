# Patrick Johnson        11/14/2019 #
# SWDV 610 3W 19/FA2    Week 4 - #3 #
#####################################
# 3. Implement a deque using linked lists

class Deque:
    """ ADT Deque implemented in Python using a Doubly Linked List

    Intrinsic Methods:
        add_first(element) - Adds reference to element to the front of the deque
        add_last(element) - Adds reference to element to the end of the deque
        delete_first() - Removes and returns the reference at the front of the deque
                         Raises an error if deque has no elements
        delete_last() - Removes and returns the reference at the end of the deque
                        Raises an error if deque has no elements

    Additional Methods:
        first() - Returns the reference to the element at the front of the deque
        last() - Returns the reference to the element at the end of the deque
        is_empty() - Returns True if the deque contains no elements
    """
    
    class _node:
        def __init__(self, data, prev_node, next_node):
            self._data = data
            self._prev = prev_node            
            self._next = next_node
    
    class EmptyDequeException(Exception):
         def __init__(self):
             super().__init__("Deque has no elements.")
    
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
        return "Deque: " + self.__str__()
        
    def is_empty(self):
        return self._front == None
        
    def add_first(self, data):
        if self._front == None: # Empty deque, new element becomes front and end
            self._front = self._node(data, None, None)
            self._end = self._front
        else:                   # New element becomes front, old front is next
            self._front = self._node(data, None, self._front)
            self._front._next._prev = self._front # Add prev link to old front
        self._count += 1        
        
    def add_last(self, data):
        if self._end == None:   # Empty deque, new element becomes front and end
            self._end = self._node(data, None, None)
            self._front = self._end
        else:                   # New element becomes end, old end is previous
            self._end = self._node(data, self._end, None)
            self._end._prev._next = self._end     # Add next link to old end
        self._count += 1
        
    def delete_first(self):
        if self._front == None:
            raise self.EmptyDequeException
        else:
            deleted_node = self._front        # Get node at front of the deque
            self._front = deleted_node._next  # Set next node as new front
            if self._front == None:  # Check if deque is empty
                self._end = None     # Remove _end reference if deque is empty
            else:                         # List is not empty
                self._front._prev = None  # Remove reference to deleted node
            self._count -= 1
            return deleted_node._data
        
    def delete_last(self):
        if self._end == None:
            raise self.EmptyDequeException
        else:
            deleted_node = self._end         # Get node at end of deque
            self._end = deleted_node._prev   # Set prev node as new end
            if self._end == None:  # Check if deque is empty
                self._front = None # Remove _front reference if deque is empty
            else:                       # List is not empty
                self._end._next = None  # Remove reference to deleted node
            self._count -= 1
            return deleted_node._data

    def first(self):
        if self._front == None:
            raise self.EmptyDequeException
        else:
            return self._front._data
        
    def last(self):
        if self._end == None:
            raise self.EmptyDequeException
        else:
            return self._end._data
        
if __name__ == "__main__":
    d = Deque()
    d.add_first(2); d.add_first(1); d.add_last(3); d.add_last(4)
    print("Deque:",d)
    print("First:",d.first())
    while not d.is_empty():
        print("Delete Last:",d.delete_last())