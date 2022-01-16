class Node:
    def __init__(self, value, next = None, previous = None):
        self.value = value
        self.next = next
        self.previous = previous
    

class DList:

    def __init__(self) :
        self.header = None
        
    

    def add_to_front(self, value):
        newNode = Node(value)
        
        if self.header == None:
            self.header = newNode
            return self
        
        
        newNode.next = self.header
        self.header.previous = newNode
        self.header = newNode

        return self
    
    def print_values(self):
        runner = self.header
        while runner != None:
            print (runner.value)
            runner = runner.next
    
    def add_to_back(self, value):
        newNode = Node(value)

        if self.header == None:
            self.header = newNode
            return self
        
        runner = self.header

        while runner.next != None:
            runner = runner.next
        
        newNode.previous = runner
        runner.next = newNode
        return self

    def add_value_by_index(self, value, index): 
        newNode = Node(value)
        if self.header == None:
            self.header = newNode
            return self
        
        runner = self.header
        i = 0

        while index != i:
            runner = runner.next
            i +=1
            if runner == None and i != index:
                print('index not found')
                return self

        if runner == None:
            self.add_to_back(newNode.value)
            return self
        else:
            newNode.next = runner
            newNode.previous = runner.previous
            runner.previous = newNode
            newNode.previous.next = newNode
            return self

        







    


myList = DList()

# myList.add_to_front(12)
# myList.add_to_front(10)
myList.add_to_back("back")
myList.add_to_front("front")
myList.add_value_by_index("Middle",2)
myList.print_values()
        
        

        
