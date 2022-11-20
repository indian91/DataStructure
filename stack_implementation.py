class UnderflowError(OverflowError):
    pass
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top == None
    
    def push(self, data): # O(1)
        node = Node(data)
        node.next = self.top
        self.top = node
    
    def pop(self): # O(1)
        if self.is_empty():
            raise UnderflowError("Stack is Empty!!")
        data = self.top.data
        self.top = self.top.next
        return data
    
    def peek(self):
        if self.is_empty():
            raise UnderflowError("Peeking From an Empty Stack")
    
    def __repr__(self):
        temp = self.top
        s = ""
        while temp:
            s += str(temp.data) + '-> '
            temp = temp.next
        s = s[:-3]
        return s
