class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start_node = Node()
    
    def add_to_start(self, data):
        node = Node(data)
        node.next = self.start_node.next
        self.start_node.next = node
    
    def add_to_end(self, data):
        node = Node(data)
        n = self.start_node
        while n.next is not None:
            n = n.next
        
        n.next = node
    
    def remove_from_start(self):
        node = self.start_node
        if node.next is None:
            print('List is empty. Nothing to delete')
        else:
            self.start_node.next = node.next
            node.next = None
            node = None
    
    def remove_from_end(self):
        node = self.start_node

        if node.next is None:
            print('List is empty. Nothing to delete')
        else:
            while node.next.next is not None:
                node = node.next
            
            node.next = None
    
    def count(self):
        c = 0
        node = self.start_node
        while node is not None:
            if node.data is not None:
                c += 1
            node = node.next

        return c
    
    def traverse(self):
        node = self.start_node
        while node is not None:
            if node.data is not None:
                print(node.data)
            node = node.next

if __name__ == '__main__':
    linkedList = LinkedList()
    number = int(input('Enter the number of nodes to be added :: '))
    for i in range(number):
        if i & 1 == 1:
            linkedList.add_to_start(int(input('Enter data :: ')))
        else:
            linkedList.add_to_end(int(input('Enter data :: ')))
    
    count = linkedList.count()
    print('Total items in list are :: {}'.format(count))

    print('Items in list are')
    linkedList.traverse()

    print('Going to delete {} items from list from end'.format(count // 2))
    for i in range(count // 2):
        linkedList.remove_from_end()
    
    count = linkedList.count()
    print('Total items in list are :: {}'.format(count))

    print('Items in list are')
    linkedList.traverse()