class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, max_entries = 5):
        self.max_entries_count = max_entries
        self.current_entries_count = 0

        # Create dummy head and tail and associate them
        self.head = Node()
        self.tail = Node()

        # Associate head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

        # maintain a hash map for easy moving of nodes
        self.hash_map = {}

    def get(self, key):
        if key in self.hash_map:
            # get the node
            node = self.hash_map[key]

            # move the node to front to indicate it is most recently used
            self.moveNode(node)

            # Return value to client
            return node.value
        else:
            # Indicates node has not been found
            return None
    
    def moveNode(self, node):
        self.removeNode(node)
        self.addNode(node)
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addNode(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def set(self, key, value):
        if key in self.hash_map:
            # Get the node
            node = self.hash_map[key]

            # update the value
            node.value = value

            # move the node to front to indicate it is most recently used
            self.moveNode(node)

            # update the hash table
            self.hash_map[key] = node
        else:
            node = Node(key, value)

            # add to front
            self.addNode(node)

            # add to hash table for next time access
            self.hash_map[key] = node

            # increment the current node counter
            self.current_entries_count += 1

            # Check if cache is full
            if self.current_entries_count > self.max_entries_count:
                self.removeLastNode()

                # reduce the counter
                self.current_entries_count -= 1
    
    def removeLastNode(self):
        node = self.tail.prev
        
        # delete it from hash map
        del self.hash_map[node.key]

        node.prev.next = self.tail
        self.tail.prev = node.prev

        node.prev = None
        node.next = None
        node = None

    def keys(self):
        node = self.head.next
        while node != self.tail:
            print(node.key)
            node = node.next

if __name__ == '__main__':
    cache = LRUCache(3)
    cache.set('name', 'Gaurav Luthra')
    cache.set('age', 30)
    cache.set('spouse', 'Bhawna')
    print('Cache keys are')
    cache.keys()
    cache.set('sex', 'M')
    print('Cache keys are')
    cache.keys()
    print('Spouse name is :: {}'.format(cache.get('spouse')))