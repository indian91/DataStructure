class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear  = None
    def is_empty(self):
        return self.front is None
    def enqueue(self, data):
        node = Node(data)
        if self.is_empty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    def dequeue(self):
        if self.is_empty():
            raise UnderFlowError("Queue is Empty")
        data = self.front.data
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        return data
    def __repr__(self):
        print("Front To Rear")
        s = ""
        temp = self.front
        while temp is not None:
            s += str(temp.data) +"-> "
            temp = temp.next
        s = s[:-3]
        return f"Queue({s})"
    
    def get_front(self):
        if self.is_empty():
            raise UnderFlowError("Queue is Empty")
        return self.front.data 
    def get_rear(self):
        if self.is_empty():
            raise UnderFlowError("Queue is Empty")
        return self.rear.data
