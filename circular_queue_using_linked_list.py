import singly_linked_list


class CircularQueue:

    def __init__(self,k) -> None:
        self.k = k
        self.queue = singly_linked_list.MyLinkedList()


    def enqueue(self,val):

        if not self.is_full():
            self.queue.add_at_tail(val)
            return True

        return False


    def dequeue(self):
        
        if self.is_empty():
            return False
        
        self.queue.delete_at_index(0)
        return True

    
    def front(self):
        if self.queue.head:
            return self.queue.head.val
        return -1

    def rear(self):
        if self.queue.tail:
            return self.queue.tail.val
        return -1

    def is_full(self):
        return self.queue.length == self.k

    def is_empty(self):
        return self.queue.length == 0



if __name__ == "__main__":

    queue = CircularQueue(5)
    queue.enqueue(5)
    print(queue.front())
    queue.dequeue()
