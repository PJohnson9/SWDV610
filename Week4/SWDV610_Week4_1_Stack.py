# Patrick Johnson        11/14/2019 #
# SWDV 610 3W 19/FA2    Week 4 - #1 #
#####################################
# 1. Implement a stack using linked lists
        
class Stack:
    """ ADT Stack implemented in Python using a Linked List

    Intrinsic Methods:
        push(element) - Adds reference to element to the top of the stack
        pop() - Removes and returns the reference to the top element
                Raises an error if stack has no elements
                
    Additional Methods:
        top() - Returns the reference to the top element of the stack
        is_empty() - Returns True if the stack contains no elements
    """
    
    class _node:
        def __init__(self, data, next_node):
            self._data = data
            self._next = next_node
    
    class EmptyStackException(Exception):
         def __init__(self):
             super().__init__("Stack has no elements.")
    
    def __init__(self):
        self._top = None
        self._count = 0
        
    def __len__(self):
        return self._count
    
    def __str__(self):
        string = "{ "
        node = self._top
        while node != None:
            string += "{" + repr(node._data) + "} "
            node = node._next
        string += "}"
        return string
    
    def __repr__(self):
        return "Stack: " + self.__str__()
        
    def is_empty(self):
        return self._top == None
        
    def push(self, data):                        # Creates new node at top of stack,
        self._top = self._node(data, self._top)  #  with previous top as _next
        self._count += 1
        
    def pop(self):
        if self._top == None:
            raise self.EmptyStackException
        else:
            popped_node = self._top          # Get node off the top of the stack
            self._top = popped_node._next    # Set next node in stack as new top
            self._count -= 1
            return popped_node._data

    def top(self):
        if self._top == None:
            raise self.EmptyStackException
        else:
            return self._top._data
    
if __name__ == "__main__":
    s = Stack()
    s.push("String"); s.push(2.718); s.push(42); s.push(3.1415926536)
    print("Stack Size:", len(s), "  Stack:", s)
    try:
        print("Pop:", s.pop())
        print("Top:", s.top())
        while True:
            print("Pop:", s.pop())
    except Stack.EmptyStackException as exception_message:
        print("Exception: ", exception_message)
        


