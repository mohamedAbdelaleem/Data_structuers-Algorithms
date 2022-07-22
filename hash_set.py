class MyHashSet:
    
    def __init__(self):
        
        self.keys = [[]] * 10

        
    def add(self, key: int):
        
        if key in self.keys[key%10]:
            pass
        else:
            self.keys[key%10].append(key)

            
    def remove(self, key: int):
        
        if key in self.keys[key%10]:
            self.keys[key%10].remove(key)

            
    def contains(self, key: int):
        
        out = key in self.keys[key%10]
        return out
        


obj = MyHashSet()
obj.add(12)
obj.remove(12)
is_contain = obj.contains(12)
print(is_contain)

