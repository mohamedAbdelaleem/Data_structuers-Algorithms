class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None

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
        curr_head = self.head
        new_head = Node(val)
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
        elif self.size == 0:
            self.head = new_node
        else:
            for i in range((self.size)-1):
                curr = curr.next
            curr.next = new_node
        self.size+=1

    def add_at_index(self, index, val):
        """
        add a node in a specific index
        """
        curr = self.head
        if index == (self.size)+1:
            self.addAtTail(val)
        elif index > (self.size)+2 or index < 0:
            pass
        elif index == 0:
            self.addAtHead(val)
        else:
            new_node = Node(val)
            for i in range(index):
                if i == index-1:
                    new_node.next = curr.next
                    curr.next = new_node
                else:
                    curr = curr.next
            self.size+=1
        

    def delete_at_index(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < self.size:
            if index == 0:
                head = self.head
                if self.size > 1:
                    self.head = head.next
                    self.size-=1
                else:
                    self.head = None
                    self.size-=1
            else:
                curr = self.head
                prev = None
                for i in range(index):
                    if i == index-1:
                        prev = curr
                        curr = curr.next
                    else:
                        curr = curr.next
                if index == (self.size)-1:
                    prev.next = None
                else:
                    prev.next = curr.next
                self.size-=1
        


obj = MyLinkedList()
obj.add_at_head(23)
obj.add_at_tail(6)
obj.add_at_index(1,5)
obj.delete_at_index(0)

print(obj.get(0))
print(obj.get(1))
