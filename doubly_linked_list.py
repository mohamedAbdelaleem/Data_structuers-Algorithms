class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def get_index(self,val):
        index = 0
        founded = False
        curr = self.head
        while curr:
            if curr.val == val:
                founded = True
                break
            index += 1
            curr = curr.next

        if not founded:
            return -1
        return index


    def get(self, index):
        """
        return the value of the needed node
        """ 
        if index >= self.length or index < 0:
            return -1
        curr_node = self.head
        for i in range(index):
            curr_node = curr_node.next
        return curr_node.val
        
        

    def add_at_head(self, val):
        """
        add a node at the first of the linked-list
        """
        new_node = Node(val)
        new_node.next = self.head
    
        if self.length == 0:
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node
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
            new_node.prev = self.tail
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
            curr = self.head
            for i in range(index):
                curr = curr.next
                
            prev_node = curr.prev
            new_node.prev = prev_node
            new_node.next = curr
            curr.prev = new_node
            prev_node.next = new_node
          
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
            
            curr = self.head
            for i in range(index):
                curr = curr.next
                
            curr.prev.next = curr.next
            if index == self.length - 1:
                self.tail = curr.prev
            else:
                curr.next.prev = curr.prev
            self.length -= 1
        


if __name__ == "__main__":
    obj = MyLinkedList()
    obj.add_at_head(12)
    obj.add_at_tail(6)
    obj.add_at_index(2,5)
    obj.delete_at_index(1)
    print(obj.get(0))
    print(obj.get(1))
