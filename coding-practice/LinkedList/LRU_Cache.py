class DLList:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRU_cache:
    def remove_node(self, node):
        prev = node.prev
        node.prev.next, node.next.prev = node.next, node.prev
    
    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def move_to_head(self, key):
        node = self.cache[key]
        self.remove_node(node)
        self.add_node(node)

    def pop_tail(self):
        to_remove = self.tail.prev
        self.remove_node(to_remove)
        return to_remove
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head, self.tail = DLList(), DLList()
        self.head.next, self.tail.prev = self.tail, self.head
        self.cache = {}
    
    def get(self, key):
        if key in self.cache:
            self.move_to_head(key)
            return self.cache[key].val
        else:
            return -1

    def put(self, key, val):
        if key not in self.cache:
            new_node = DLList(key, val)
            self.add_node(new_node)
            self.cache[key] = self.head.next
            self.size += 1
        else:
            self.move_to_head(key)
            self.cache[key].val = val
        if self.size > self.capacity:
            k = self.pop_tail()
            del self.cache[k.key]
            self.size -= 1

testcases = [[["LRUCache","put","get","put","get","get"], [[1],[2,1],[2],[3,2],[2],[3]]], [["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"], [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]], [["LRUCache","put","put","get","put","put","get"], [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]]]
lru_obj = None

for t in testcases:
    for t, p in zip(t[0], t[1]):
        if t == "LRUCache":
            lru_obj = LRU_cache(p[0])
        elif t == "put":
            lru_obj.put(p[0], p[1])
        else:
            print(f'GET {lru_obj.get(p[0])}')
    print()
