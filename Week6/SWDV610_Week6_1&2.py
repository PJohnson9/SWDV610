# Patrick Johnson        11/30/2019 #
# SWDV 610 3W 19/FA2   Week 6 - 1&2 #
#####################################

# 1. Generate a random list of integers.  Show the binary heap tree 
#    resulting from inserting the integers on the list one at a time.
#    
# 2. Using the list from the previous question, show the binary heap tree 
#    resulting from the list as a parameter to the buildHeap method. 

class BinHeap:
    """ Binary Heap Implementation
    Most of class using code from Problem Solving with Algorithms and Data Structures using Python
    by Brad Miller and David Ranum
    https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html
    
    Directly copied from source:
        BinaryHeap() creates a new, empty, binary heap.

        insert(k) adds a new item to the heap.

        buildHeap(list) builds a new heap from a list of keys.

        delMin() returns the item with the minimum key value, removing the item from the heap.
        
    Described in source, but implemented by Patrick Johnson:

        findMin() returns the item with the minimum key value, leaving item in the heap.

        isEmpty() returns true if the heap is empty, false otherwise.

        size() returns the number of items in the heap.

    Extended with printList and printTree methods by Patrick Johnson on November 30, 2019
    """
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
            
    def size(self):
        """ Returns size of the heap
        Method implemented by Patrick Johnson November 30, 2019
        """
        return self.currentSize
    
    def isEmpty(self):
        """ Returns true if the heap is empty
        Method implemented by Patrick Johnson November 30, 2019
        """
        return 0 == self.currentSize
    
    def findMin(self):
        """ Returns the value of the smallest item on the heap.
        Method implemented by Patrick Johnson November 30, 2019
        """
        return self.heapList[1]
            
    # Additional Methods
    def printList(self):
        """ Print a list view of the binary heap
        Method created by Patrick Johnson November 30, 2019
        """
        print(self.heapList[1:])
    
    def printTree(self):
        """ Print a tree view of the binary heap
        Method created by Patrick Johnson November 30, 2019
        """
        from math import log, ceil
        tree_depth = ceil(log(self.currentSize+1,2))
        level = 1
        item = 1
        while level <= tree_depth:
            print('|', end='')
            while item < 2**level and item <= self.currentSize:
                print("{}".format(self.heapList[item]).center(6*2**(tree_depth-level)-1), end= '|')
                item += 1
            print('')
            level += 1


if __name__ == "__main__":
    from random import randint, seed
    # Generate random list (Seed specified for repeatability)
    seed(3.14)
    l = []
    for ri in range(15):
        l.append(randint(0,60))
    # l = [31, 48, 3, 23, 17, 1, 48, 47, 41, 9, 54, 29, 8, 24, 30]


    # Problem #1 
    print("Random List: ", l)
    print()
    print("1. Inserted item by item:")
    heap = BinHeap()
    for item in l:
        heap.insert(item)
    print("Heap List:    ", end='')
    heap.printList()
    print("Tree View:")
    heap.printTree()
    print()


    # Problem #2
    print("2. Built from list:")
    heap.buildHeap(l)
    print("Heap List:    ", end='')
    heap.printList()
    print("Tree View:")
    heap.printTree()

