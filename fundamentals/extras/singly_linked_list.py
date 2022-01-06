class Node:
    def __init__(self, value) :
        self.value = value
        self.next = None



class SList:
    def __init__(self):
        self.header = None
    

    def add_to_front(self,value):
        newNode = Node(value)
        newNode.next = self.header
        self.header = newNode
        return self
    
    def print_values(self):
        runner = self.header
        while (runner != None):
            print(runner.value)
            runner = runner.next

    def add_to_back (self,value):
        if self.header == None:
            self.add_to_front(value)
        else:
            newNode = Node(value)
            runner = self.header
            while (runner.next != None):
                runner = runner.next
            runner.next = newNode
        return self
    
    def remove_from_front(self): 
        removeValue = self.header
        self.header = removeValue.next
        del removeValue

    def remove_from_back(self):
        if self.header != None:
            previousVal = self.header
            nextValue = previousVal.next
            while (nextValue.next != None):
                previousVal = nextValue
                nextValue = previousVal.next
            previousVal.next = None
            del nextValue
        return self
    
    def insert_at(self,value, n ):
        

        if self.header == None or n == 0:
            self.add_to_front(value)
        
        else:
            newNode = Node(value)
            index = 0
            prevValue = self.header
            nextValue = prevValue.next

            while (index+1 < n ):
                if nextValue == None:
                    raise UnboundLocalError
                prevValue = nextValue
                nextValue = prevValue.next
                index += 1
            
            prevValue.next = newNode
            newNode.next = nextValue
            return self
        
        
        
        




new_list = SList()
new_list.add_to_front(10)
new_list.add_to_front(12)
new_list.add_to_front(0)
new_list.add_to_front("the front")
new_list.add_to_back("I am at the back")
new_list.print_values()
print('\n')
new_list.insert_at("new",4)
new_list.print_values()
