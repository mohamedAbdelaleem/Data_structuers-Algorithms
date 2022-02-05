class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None]*k 
        self.head = -1
        self.tail = -1
        self.length = 0

    def en_queue(self, value: int) -> bool:
        """ Add an element to the queue 'after the current tail' """
        if self.length < self.k:
            if self.head == -1:
                self.head += 1
            if self.tail == (self.k)-1:
                self.tail = 0
            else:
                self.tail += 1
            self.queue[self.tail] = value
            self.length+=1
            return True
        
        else:
            return False

    def de_eueue(self) -> bool:
        """ delete an element from the queue 'the current head' """
        if self.length ==0 :
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
                

    def front(self) -> int:
        """ return the head """
        if self.queue[self.head]:
            return self.queue[self.head]
        elif self.queue[self.head] == 0:
            return 0
        else:
            return -1

    def rear(self) -> int:
        """ return the tail """
        if self.queue[self.tail]:
            return self.queue[self.tail]
        elif self.queue[self.tail] == 0:
            return 0
        else:
            return -1

    def is_empty(self) -> bool:
        if self.length == 0:
            return True
        else:
            return False

    def is_full(self) -> bool:
        if self.length == self.k:
            return True
        else:
            return False


obj = MyCircularQueue(3)
obj.en_queue(12)
obj.en_queue(0)
obj.de_eueue()
print(obj.front())
print(obj.rear())
print(obj.is_empty())
print(obj.is_full())
