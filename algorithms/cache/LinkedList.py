class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def add_to_start(self, key, value):
        node = Node(key, value)
        node.ref = self.start_node
        self.start_node = node

    def add_at_end(self, key, value):
        node = Node(key, value)
        n = self.start_node
        if n is None:
            self.start_node = node
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = node

    def add_after_value(self, x, key, value):
        node = Node(key, value)
        n = self.start_node
        if n is None:
            self.start_node = node
        else:
            while n.key != x:
                n = n.ref
            node.ref = n.ref
            n.ref = node

    def remove_from_last(self):
        if self.start_node is None:
            print('List is empty. Nothing to remove')
        else:
            node = self.start_node
            if node.ref is None:
                node = None
            while node.ref.ref is not None:
                node = node.ref
            node.ref = None
        
    def remove_with_value(self, x, key, value):
        if self.start_node is None:
            print('List is empty. Nothing to remove')
        else:
            node = self.start_node
            # Handle first item
            if node.ref is None and node.key == x:
                node = None

            while node.ref is not None:
                if node.ref.key == x:
                    break
                node = node.ref
            
            if node.ref is None:
                print('Item note found')
            else:
                node.ref = node.ref.ref

    def traverse_list(self):
        node = self.start_node
        while node is not None:
            print(node.key)
            node = node.ref

if __name__ == '__main__':
    linked_list = LinkedList()
    nodes_count = int(input('Enter the number of nodes :: '))
    for i in range(nodes_count):
        key = int(input('Enter the node key :: '))
        linked_list.add_at_end(key, 1)

    linked_list.traverse_list()
