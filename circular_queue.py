class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None]*k 
        self.head = -1
        self.tail = -1
        self.length = 0

    def en_queue(self, value: int):
        """ Add an element to the queue 'after the current tail' """
        if self.length < self.k:
            if self.head == -1:
                self.head += 1
            if self.tail == (self.k)-1:    # if the current tail is the last element then the next element should be assigned to index 0
                self.tail = 0              
            else:
                self.tail += 1
            self.queue[self.tail] = value
            self.length+=1
            return True
        
        else:
            return False

    def de_eueue(self):
        """ delete an element from the queue 'the current head' """
        if self.is_empty() :
            return False
        else:
            self.queue[self.head] = None
            self.length-=1
            if self.head == (self.k)-1:
                if self.length > 0:
                    self.head = 0
                else:
                    self.head = -1
                    self.tail = -1
            else:
                self.head += 1
            return True
                

    def front(self):
        """ return the head """
        if self.is_empty():
            return -1
        return self.queue[self.head]

    def rear(self):
        """ return the tail """
        if self.is_empty():
            return -1
        return self.queue[self.tail]

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.k


obj = MyCircularQueue(3)
obj.en_queue(12)
obj.en_queue(0)
obj.de_eueue()
print(obj.front())
print(obj.rear())
print(obj.is_empty())
print(obj.is_full())
