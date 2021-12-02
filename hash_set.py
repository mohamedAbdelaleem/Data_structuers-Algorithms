class MyHashSet:
    
    def __init__(self):
        
        self.keys = []

        
    def add(self, key: int):
        
        if key in self.keys:
            pass
        else:
            self.keys.append(key)

            
    def remove(self, key: int):
        
        if key in self.keys:
            self.keys.remove(key)

            
    def contains(self, key: int):
        
        out = key in self.keys
        return out
        


obj = MyHashSet()
obj.add(12)
obj.remove(12)
is_contain = obj.contains(12)
print(is_contain)
