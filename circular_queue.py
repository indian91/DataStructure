class CircularQueue:
    def __init__(self, size=5):
        self.size = size
        self.front = -1
        self.rear  = -1
        self.data = [ None ] * self.size
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        cond =[
            ((self.rear == self.size - 1) and self.front == 0),
            self.rear == self.front - 1
        ]
        return any(cond)
    def enqueue(self, data):
        if self.is_full():
            raise OverflowError("Queue is Full")
        if self.front == -1:
            self.front += 1
        if self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.data[self.rear] = data # O(1)
    def dequeue(self):
        if self.is_empty():
            raise UnderFlowError("Queue is Empty")
        data = self.data[self.front]
        self.data[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1
        return data
            
    def __repr__(self):
        return f"CircularQueue({self.data})"
