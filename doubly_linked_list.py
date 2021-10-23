class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index):
        """
        return the value of the needed node
        """            
        if index >= self.size or index < 0:
            return -1
        
        curr = self.head
        if curr is None:
            return -1
        if index == 0:
            return curr.val
        for i in range(index):
            curr = curr.next
        return curr.val
        
        

    def add_at_head(self, val):
        """
        add a node at the first of the linked-list
        """
        new_head = Node(val)
        if self.head is None:
            self.head = new_head
        else:
            curr_head = self.head
            curr_head.prev = new_head
            new_head.next = curr_head
            self.head = new_head
        self.size+=1
        

    def add_at_tail(self, val):
        """
        add a node at the end of the linked-list
        """
        new_node = Node(val)
        curr= self.head
        if self.size == 1:
            curr.next = new_node
            new_node.prev = curr
        elif self.size == 0:
            self.head = new_node
        else:
            for i in range((self.size)-1):
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
        self.size+=1

    def add_at_index(self, index, val):
        """
        add a node in a specific index
        """
        curr = self.head
        if index == (self.size):
            self.add_at_tail(val)
        elif index > (self.size) or index < 0:
            pass
        elif index == 0:
            self.add_at_head(val)
        else:
            new_node = Node(val)
            for i in range(index):
                if i == index-1:
                    n = curr.next
                    new_node.next = n
                    new_node.prev = curr
                    curr.next = new_node
                    n.prev = new_node
                else:
                    curr = curr.next
            self.size+=1
        

    def delete_at_index(self, index):
        """
        delete the node that its index is the given index 
        """
        if index < self.size:
            if index == 0:
                head = self.head
                if self.size > 1:
                    self.head = head.next
                    self.head.prev = None
                    self.size-=1
                else:
                    self.head = None
                    self.size-=1
            else:
                curr = self.head
                for i in range(index):
                    curr = curr.next
                prev = curr.prev
                    
                if index == (self.size)-1:
                    prev.next = None
                else:
                    n = curr.next
                    prev.next = n
                    n.prev = prev
                self.size-=1
        


obj = MyLinkedList()
obj.add_at_head(12)
obj.add_at_tail(6)
obj.add_at_index(3,5)
obj.delete_at_index(1)
print(obj.get(0))
print(obj.get(1))
