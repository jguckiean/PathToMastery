import Utilities as Util

class Stack():
    top = -1
    capacity = 0
    arrayForStacking = []  
    
    def __init__(self, capacity):
        self.arrayForStacking = [None] * capacity
        self.capacity = capacity
    
    def IsOverFlow(self):
        return self.top is (self.capacity - 1)
    
    def IsUnderFlow(self):
        return self.top is -1

    def push(self, input):
        if self.IsOverFlow():            
            Util.TriggerStackOverFlowError()        
        else:  
            self.top = self.top + 1          
            self.arrayForStacking[self.top] = input
            

    def pop(self):
        if self.IsUnderFlow():           
            Util.TriggerStackUnderFlowError()        
        else:
            toBePoppedValue = self.arrayForStacking[self.top]
            self.top = self.top - 1           
            return toBePoppedValue
            
