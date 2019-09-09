class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, max_entries = 5):
        self.max_entries_count = max_entries
        self.current_entries_count = 0

        # Create dummy head and tails
        self.head = Node()
        self.tail = Node()

        # Associate head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

        # maintain a hash table for faster deletion and moving the nodes
        self.hash_table = {}

    # Given a key, it fetches the value
    def get(self, key):
        if key in self.hash_table:
            # O(1) access from hash table
            node = self.hash_table[key]

            # we got the node, now move the node to front
            # This indicates that it is most recently accessed node
            # This is done in constant time O(1)
            self.moveNode(node)

            # return value to client
            return node.value
        else:
            # -1 indicates no item is found
            return -1
    
    # move the node to front
    def moveNode(self, node):
        # first remove node from its position - O(1)
        # add it to front - O(1)
        self.removeNode(node)
        self.addNode(node)

    # remove node from its position O(1)
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    # add node to begining
    def addNode(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    # Set aka update the cache
    def set(self, key, value):
        # first check if this key is in hash table - O(1)
        if key in self.hash_table:
            # We need to update the value
            # also move the node to front to indicate it is most recently used
            node = self.hash_table[key]
            node.value = value
            
            # Update the hash table - O(1)
            self.hash_table[key] = node

            # Move node to front - O(1)
            self.moveNode(node)
        else:
            # It is new key/value pair
            node = Node(key, value)

            # add this node to front - O(1)
            self.addNode(node)

            # add this node to hash table - O(1)
            self.hash_table[key] = node

            # update the counter
            self.current_entries_count += 1

            # if it reaches the threshold then remove the least recently used entry
            if self.current_entries_count > self.max_entries_count:
                self.removeLastNode()

                # remove entry from hash table - O(1)
                del self.hash_table[key]

                # reduce the current entries count
                self.current_entries_count -= 1

    # remove last node - O(1)
    def removeLastNode(self):
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail

        node.next = None
        node.prev = None

    # Get all keys from cache - O(N)
    def keys(self):
        items = []
        node = self.head.next
        while node is not None:
            if node.key is not None:
                items.append(node.key)
            node = node.next
        return items

if __name__ == '__main__':
    cache = LRUCache(3)
    cache.set('name', 'Gaurav')
    cache.set('age', 30)
    cache.set('spouse', 'Bhawna')
    print('Name is : {}'.format(cache.get('name')))
    print('All keys in cache are :: {}'.format(cache.keys()))
