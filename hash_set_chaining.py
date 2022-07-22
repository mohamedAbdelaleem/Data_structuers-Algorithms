import doubly_linked_list as db


def hash_func(key):

    return abs(hash(key)) % 100


class HashSet:

    def __init__(self) -> None:
        self.hash_set = [db.MyLinkedList()] * 100
        

    def add(self,key):
        key_hash = hash_func(key)
        index = self.hash_set[key_hash].get_index(key)
        if index == -1:             # then it doesn't exist, that for prevent adding duplicates
            self.hash_set[key_hash].add_at_tail(key)
    

    def contains(self,key):
        key_hash = hash_func(key)
        curr =  self.hash_set[key_hash].head
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False
    
    def remove(self,key):
        key_hash = hash_func(key)
        linked_list = self.hash_set[key_hash]
        index = linked_list.get_index(key)
        linked_list.delete_at_index(index)
        

if __name__ == "__main__":
    hash_set = HashSet()
    hash_set.add(12)
    hash_set.add("cs1")
    print(hash_set.contains(12))
    print(hash_set.contains("cs1"))
    hash_set.remove("cs1")
    print(hash_set.contains("cs1"))





