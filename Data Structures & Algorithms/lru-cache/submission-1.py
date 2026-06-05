#Create Node func with key and val fields
class Node:
    
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity #capacity as cap
        self.cache = {} #hashmap to store Node(key,val)

        #Create and define doubly linked list
        self.left, self.right = Node(0,0), Node(0,0) #Create Dummy nodes
        self.left.next, self.right.prev = self.right, self.left # Node(k,v)<=>Node(k,v)

    def insert(self, node):
        prv, nxt = self.right.prev, self.right #take the two end nodes as prv and nxt
        prv.next = nxt.prev = node #insert node in middle: prv<=>node<=> nxt
        node.prev, node.next = prv, nxt #point the node to make double link

    def remove(self, node):
        prv, nxt = node.prev, node.next #gets the nodes at either side of cur node
        prv.next, nxt.prev =  nxt, prv # Node()<=>Node()<=>Node() !!make smaller

        
    def get(self, key: int) -> int:
        if key in self.cache:           # reenter value to make it most recent and return val
            self.remove(self.cache[key]) 
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:           #removes val first and enters it again
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) #Creates new Node
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            LRU = self.left.next 
            self.remove(LRU) #remove lru node
            del self.cache[LRU.key] #remove lry from cache/hashmap
