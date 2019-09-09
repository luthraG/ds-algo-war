class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    # Here main logic is to 
    def __init__(self, max_entries):
        self.hashtable = {}
        self.headNode = Node(-1002, -1002)
        self.tailNode = Node(-1002, -1002)
        self.maxEntries = max_entries
        self.currentTotal = 0

        # associate head node and tail node
        self.headNode.next = self.tailNode
        self.tailNode.prev = self.headNode
    
    def get(self, key):
        # This implements the get method of cache
        if key in self.hashtable:
            node = self.hashtable[key]
            # Move node at the begining to make it most recently used
            self.moveNode(node)

            # Return value of node to client
            return node.value
        else:
            # value does not exists and hence return -1001
            return -1001

    def set(self, key, value):
        # Check if it already exists
        if key in self.hashtable:
            node = self.hashtable[key]
            node.value = value
            # Move node at the begining to make it most recently used
            self.moveNode(node)
            # Update the hashtable
            self.hashtable[key] = node
        else:
            # Does not exists in hashtable so we need to insert
            node = Node(key, value)
            # add node at the begining
            self.addNode(node)
            # Increment the node counter
            self.currentTotal += 1
            # print("{} for {}".format(self.currentTotal, key))

            # Update hashtable
            self.hashtable[key] = node
            if self.currentTotal > self.maxEntries:
                # Remove the node
                self.removeLastNode()


    def moveNode(self, node):
        self.removeNode(node)
        self.addNode(node)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addNode(self, node):
        self.headNode.next.prev = node
        node.next = self.headNode.next
        node.prev = self.headNode
        self.headNode.next = node
    
    def removeLastNode(self):
        lastNode = self.tailNode.prev
        key = lastNode.key
        # print(lastNode.key)
        lastNode.prev.next = self.tailNode
        self.tailNode.prev = lastNode.prev
        lastNode = None

        # Reduce the current nodes counter
        self.currentTotal -= 1

        # Remove entry from hashtable
        del self.hashtable[key]

    def cacheKeys(self):
        print('Total keys :: {}'.format(self.currentTotal))
        node = self.headNode
        while node.next is not None:
            if node.key != -1002:
                print(node.key)
            node = node.next

if __name__ == '__main__':
    cache = LRUCache(5)
    cache.set("name", "gaurav")
    cache.set("age", 30)
    cache.set("sex", "M")
    cache.set("salary", "120K")
    cache.set("spouse", "bhawna")
    cache.set("success", True)
    cache.set("success1", False)
    # print(cache.get("name"))
    cache.cacheKeys()
