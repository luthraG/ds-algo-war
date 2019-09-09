class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, max_entries):
        # Controls when to evict an entry from cache
        self.max_entries = max_entries
        self.current_entries = 0

        # For faster look up O(1)
        self.hash_table = {}

        # Get dummy head and tail
        self.head = Node()
        self.tail = Node()

        # Associate head and tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # Given a key find the value
    def get(self, key):
        if key in self.hash_table:
            # Fetch the node
            node = self.hash_table[key]
            # Move the node to front
            self.moveNode(node)
            # Return the value
            return node.value
        else:
            # Node not in hash_table
            return -1

    def moveNode(self, node):
        self.removeNode(node)
        self.addNode(node)

    def removeNode(self, node):
        # Removed node from its position - It can be anywhere in linkedlist
        node.prev.next = node.next
        node.next.prev = node.prev

    def addNode(self, node):
        # Node is always added at front
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node

    def set(self, key, value):
        # Check if already exists in hash_table
        # If yes then just update the value
        # Move node to front
        if key in self.hash_table:
            node = self.hash_table[key]
            node.value = value
            self.moveNode(node)
            # Update hashtable
            self.hash_table[key] = node
        else:
            # It is new item to be inserted
            # New item is always inserted at front
            # Once added, increment the current nodes count
            # Add entry in hash_table
            # If it exceeded then max allowed count then
            # remove the last node and decrement the count
            node = Node(key, value)
            # Adds the node to front
            self.addNode(node)
            # Increment the counter
            self.current_entries += 1
            # Update the hash_table
            self.hash_table[key] = node

            if self.current_entries > self.max_entries:
                self.removeLastNode()
    
    def removeLastNode(self):
        # Removes the last node
        # decrement the current entries counter
        # Remove from hash_table
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail

        key = node.key
        node.next = None
        node.prev = None
        node = None

        self.current_entries -= 1

        del self.hash_table[key]
    
    def cacheKeys(self):
        for key in self.hash_table:
            print(key)

if __name__ == '__main__':
    cache = LRUCache(5)
    cache.set('name', 'gaurav')
    cache.set('age', 30)
    cache.set('sex', 'M')
    cache.set('company', 'Netflix')
    cache.set('salary', '250K')
    print(cache.get('name'))
    # cache.cacheKeys()