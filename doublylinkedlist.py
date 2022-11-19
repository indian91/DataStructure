class UnderFlowError(OverflowError):
    pass
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None       
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __repr__(self):
        temp=self.head
        item=''
        while temp!=None:
            item+=str(temp.data) + " <-> " 
            temp=temp.next
        return f"LinkedList({item[:-4]})"
    def is_empty(self):
        if self.head==None:
            return True
        return False
    def append(self,node):
        if self.is_empty():
            self.head=node
            self.tail=node
        else:
            node.prev=self.tail
            self.tail.next=node
            self.tail=node  
    def insert_at_first(self,node):
        if self.is_empty():
            self.append(node)
        else:
            temp=self.head
            self.head=node
            node.next=temp
            node.prev=None
    def insert_at_loc(self,loc,node):
        if loc==0:
            self.insert_at_first(node)
        elif self.is_empty():
            #self.append(node)
            raise IndexError("LinkedList is empty, please insert at 0 location")
        else:
            temp=self.head
            c=0
            while c<loc-1 and temp.next!=None:
                #print(temp.data)
                temp=temp.next
                c+=1
            if temp.next!=None:
                node.prev=temp
                node.next=temp.next
                temp.next=node
            else:
                raise IndexError("Index out of range...")
    def remove_from_last(self):
        if self.is_empty():
            raise UnderFlowError("LinkedList is empty...")
        elif self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            temp=self.tail.prev
            self.tail=temp
            temp.next=None
    def remove_from_first(self):
        if self.is_empty():
            raise UnderFlowError("LinkedList is empty...")
        elif self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            temp=self.head.next
            self.head=temp
            temp.prev=None  
    def remove_from_loc(self,loc):
        if loc==0:
            self.remove_from_first()
        elif self.is_empty():
            #self.append(node)
            raise IndexError("LinkedList is empty...")
        else:
            temp=self.head
            c=0
            while c<loc-1 and temp.next!=None:
                #print(temp.data)
                temp=temp.next
                c+=1
            if temp.next!=None:
                temp.next=temp.next.next
                temp.next.prev=temp
            else:
                raise IndexError("Index out of range...")  
    def remove_element(self,ele):
        if self.is_empty():
            raise IndexError('LinkedList is empty...')
        elif self.head.data==ele:
            self.remove_from_first()
        else:
            temp=self.head
            while temp.next!=None:
                if temp.next.data==ele:
                    temp.next=temp.next.next
                    temp.next.prev=temp
                    break
                else:
                    temp=temp.next
            else:
                raise IndexError("No Element Found...")
                
    def reverse(self):
        temp=self.tail
        new=DoublyLinkedList()
        while temp!=None:
            new.append(Node(temp.data))
            temp=temp.prev
        return new
