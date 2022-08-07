class Node:
    
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index):
        """
        return the value of the needed node
        """            
        if index >= self.length or index < 0:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val
        
        

    def add_at_head(self, val):
        """
        add a node at the first of the linked-list
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1
        

    def add_at_tail(self, val):
        """
        add a node at the end of the linked-list
        """
        new_node = Node(val)
        if self.length == 0:
            self.add_at_head(val)
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def add_at_index(self, index, val):
        """
        add a node in a specific index
        """
        if index == 0:
            self.add_at_head(val)
        elif index == self.length:
            self.add_at_tail(val)
        elif 0 < index < self.length:
            
            new_node = Node(val)
            prev = self.head
            for i in range(index-1):
                prev = prev.next
                
            next_node = prev.next
            prev.next = new_node
            new_node.next = next_node
            self.length += 1

        

    def delete_at_index(self, index):
        """
        delete the node that its index is the given index 
        """
        if index == 0 and self.length >= 1:
            node = self.head.next
            self.head = node
            if self.length == 2:
                self.tail = node
            self.length -= 1
        
        elif 0 < index < self.length:
            
            prev = self.head
            for i in range(index-1):
                prev = prev.next
                
            prev.next = prev.next.next
            if index == self.length - 1:
                self.tail = prev
            self.length -= 1        


if __name__ == "__main__":
    obj = MyLinkedList()
    obj.add_at_head(23)
    obj.add_at_tail(6)
    obj.add_at_index(1,5)
    obj.delete_at_index(0)

    print(obj.get(0))
    print(obj.get(1))
