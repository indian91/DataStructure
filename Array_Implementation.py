class StackOverFlowError(OverflowError):
    pass

class StackUnderFlowError(OverflowError)
    pass

class Array:
    
    
    def __init__(self,size):
        self.__size = size
        self.__index=-1
        self.__data=[None for i in range(size)]
        
    def __str__(self):
        items=""
        for i in self.__data:
            if i==None:
                break
            items+=str(i)+', '
        return f"Array({items})"
    def is_full(self):
        if self.__index == self.__size-1:
            return True
        return False
    def append(self, element):
        if self.is_full():
            self.resize_array()
        self.__index+=1
        self.__data[self.__index]=element
    def resize_array(self):
        new_data=[None for i in range(self.__size*2)]
        for i in range(self.__size):
            new_data[i]=self.__data[i]
        self.__data=new_data
        self.__size*=2
        
    def insert(self,loc,element):
        if self.is_full():
            self.resize_array()
        if loc > self.__index:
            print("Hey")
            self.append(element)
        elif loc<0:
            raise IndexError("Negative Index")
        else:
            j=self.__index
            self.__index+=1
            while j >= loc:
                self.__data[j+1]=self.__data[j]
                j=j-1
            self.__data[loc]=element
    def is_empty(self):
        if self.__index==-1:
            return True
        return False
    def pop(self,loc=None):
        if self.is_empty():
            raise StackUnderFlowError("Stack is empty")
        elif loc is None:
            slef.__data[index]=None
            self.__index-=1
        elif loc>self.__index or loc<-1:
            raise IndexError("Array Index Out of Range")
        else:
            item = self.__data[loc]
            while loc < self.__index:
                self.__data[loc]=self.__data[loc+1]
                loc+=1
            self.__index-=1
            self.__data[loc]=None
            return item
    @property
    def size(self):
        return self.__size
