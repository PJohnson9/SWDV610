# Patrick Johnson        11/30/2019 #
# SWDV 610 3W 19/FA2   Week 6 - 3&4 #
#####################################

# Optional Bonus Questions:
# 3. Extend the buildParseTree function to handle mathematical expressions
#    that do not have spaces between every character.
#
# 4. Extend the buildParseTree and evaluate functions to handle boolean
#    statements. Remember that "not" is a unary operator, so this will
#    complicate your code somewhat.

class Stack:
    """ Copied from Activity 1 at:
https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaStackinPython.html
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class BinaryTree:
    """ Mostly copied from Activity 1 at:
https://runestone.academy/runestone/books/published/pythonds/Trees/NodesandReferences.html

    Preorder, inorder, and postorder methods from:
https://runestone.academy/runestone/books/published/pythonds/Trees/TreeTraversals.html    
    """
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        """
        Copied from Listing 3 at:
        https://runestone.academy/runestone/books/published/pythonds/Trees/TreeTraversals.html
        """
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
            
    def postorder(self):
        """
        Adapted from Listing 4 at:
        https://runestone.academy/runestone/books/published/pythonds/Trees/TreeTraversals.html
        """
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)
        

    def inorder(self):
        """
        Adapted from Listing 6 at:
        https://runestone.academy/runestone/books/published/pythonds/Trees/TreeTraversals.html
        """
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()
            
def printexp(tree):
    """ Based on code from Listing 7 at:
    https://runestone.academy/runestone/books/published/pythonds/Trees/TreeTraversals.html
    
    Modified to include spaces around operators (excluding '~') and parentheses
    """
    sVal = ''
    if tree:
        if tree.getLeftChild():
            sVal = ' (' + printexp(tree.getLeftChild())
        else:
            sVal = ' '
            
        sVal = sVal + str(tree.getRootVal())
        
        if tree.getRightChild():
            if tree.getRootVal() == '~':
                sVal = sVal + printexp(tree.getRightChild())[1:]
            elif tree.getRootVal() == 'NOT':
                sVal = sVal + printexp(tree.getRightChild())
            else:
                sVal = sVal + printexp(tree.getRightChild())+') '
        else:
            sVal = sVal + ' '
    return sVal

def buildParseTree(fpexp):
    """ Adapted from Activity 1 at:
https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html

    Notable changes:
        Additional operators added
        Able to parse expressions without spaces around all operators and paretheses
        Can handle unary operators
    """
    binary_operators = ['+', '-', '*', '/', '&', '|', "AND", "OR"]
    unary_operators = ['~', "NOT"]
    parentheses = ['(',')']
    operators = binary_operators + unary_operators
    
    # Adds spaces around operators and parentheses [Problem #3]
    for o in operators + parentheses:
        fpexp = fpexp.replace(o, ' '+o+' ')
    
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in operators:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()
            
            # Climb back up stack without ) through unary operators [Problem #4]
            while currentTree.getRootVal() in unary_operators:
                currentTree = pStack.pop()

        else:
            try:
                # Additional code for parsing logical keywords [Problem #4]
                if i.capitalize() == 'True':
                    currentTree.setRootVal(True)
                elif i.capitalize() == 'False':
                    currentTree.setRootVal(False)
                else: # Not True/False, so try parsing as int
                    currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent
                
                # Climb back up stack without ) through unary operators [Problem #4]
                while currentTree.getRootVal() in unary_operators:
                    currentTree = pStack.pop()

            except ValueError:
                raise ValueError("token '{}' is not a valid integer or boolean".format(i))

    return eTree

## Testing Code
#exp2 = "( ( 10 + 5 ) * 3 )"
#pt2 = buildParseTree(exp2)
#print("Original Expression:  ", exp2)
#print("Expression from Tree:", printexp(pt2))
#
#exp3 = "( ( 1 & 0 ) | ~( ~1 & ~0 ) )"
#pt3 = buildParseTree(exp3)
#print("Original Expression:  ", exp3)
#print("Expression from Tree:", printexp(pt3))
#pt3.postorder()


# Examples for Demonstration
print("Example 1:")
exp1 = "( ( 10 + 5 ) * 3 )"
pt1 = buildParseTree(exp1)
print("Original Expression:  ", exp1)
print("Post-Order Tree Traversal:")
pt1.postorder()
print("Expression from Tree:", printexp(pt1))

print("\nExample 2 (no spaces):")
exp2 = "((10+5)*3)"
pt2 = buildParseTree(exp2)
print("Original Expression:  ", exp2)
print("Expression from Tree:", printexp(pt2))

print("\nExample 3 - Logical Symbols:")
exp3 = "( ( 1 & 0 ) | ~1 )"
pt3 = buildParseTree(exp3)
print("Original Expression:  ", exp3)
print("Expression from Tree:", printexp(pt3))
print("Post-Order Tree Traversal:")
pt3.postorder()

print("\nExample 4 - Logical Keywords:")
exp4 = "( ( 1 AND 0 ) OR NOT 1 )"
pt4 = buildParseTree(exp4)
print("Original Expression:  ", exp4)
print("Expression from Tree:", printexp(pt4))

print("\nExample 5 - Logical Keywords II:")
exp5 = "( ( False AND True ) OR NOT ( NOT False OR NOT True ) )"
pt5 = buildParseTree(exp5)
print("Original Expression:  ", exp5)
print("Expression from Tree:", printexp(pt5))