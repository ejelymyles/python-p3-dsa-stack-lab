import ipdb 
class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        

    def isEmpty(self):
        return len(self.items) == 0
        

    def push(self, item):
        if len(self.items) != self.limit:
            self.items.append(item)
    
           
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None
        

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)
        

    def full(self):
        return self.size() >= self.limit
       
        
    def search(self, target):
        distance = self.size()
        for value in self.items:
            # ipdb.set_trace()
            if value != target:
                distance -= 1
            else:
                return distance - 1

        return -1
        