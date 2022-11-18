class LinkedListUnderFlowError(Exception):
    pass

class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    
    def __init__(self):
        self.head=None
        self.tail=None
    def __repr__(self):
        temp=self.head
        item=''
        while temp!=None:
            item+=str(temp.data) + "-> " 
            temp=temp.next
        return f"{item[:-3]}"
    def is_empty(self):
        if self.head==None:
            return True
        return False
    def append(self,node):
        if self.is_empty():
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def remove_from_last(self):
        if self.is_empty():
            raise LinkedListUnderFlowError("Linked List is Empty...")
        elif self.head.next==None:
            self.head=self.tail=None
        else:
            temp = self.head
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
            self.tail=temp
            
    def remove_from_first(self):
        
        if self.is_empty():
            raise LinkedListUnderFlowError("Linked List is Empty...")
        elif self.head.next==None:
            self.head=self.tail=None
        else:
            self.head=self.head.next
            
    def remove_by_element(self,element):
        
        if self.is_empty():
            raise LinkedListUnderFlowError("Linked List is Empty...")
        elif self.head.data==element:
            self.remove_from_first()
        else:
            temp=self.head
            try:
                while temp.next.data!=element:
                    temp=temp.next
            except:
                return -1
            else:
                temp.next=temp.next.next
