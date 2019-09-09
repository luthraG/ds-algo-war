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
        n = self.start_node
        while n.next is not None:
            n = n.next
        
        node = Node(data)
        n.next = node

    def remove_from_start(self):
        n = self.start_node.next
        if n is None:
            print('List is empty')
        else:
            self.start_node.next = n.next
            n.next = None
            n = None

    def remove_from_last(self):
        n = self.start_node
        if n.next is None:
            print('List is empty')
        else:
            while n.next.next is not None:
                n = n.next
            
            n.next = None

    def travese_from_start(self):
        node = self.start_node
        while node is not None:
            if node.data is not None:
                print(node.data)
            node = node.next

if __name__ == '__main__':
    linkedList = LinkedList()
    number_start = int(input('Enter number of items to be added at start :: '))
    number_end = int(input('Enter number of items to be added at last :: '))

    for i in range(number_start):
        data = int(input('Enter item to be added at start :: '))
        linkedList.add_to_start(data)

    print('Items in the list now...')
    linkedList.travese_from_start()
    print('------------------------')

    for i in range(number_end):
        data = int(input('Enter item to be added at end :: '))
        linkedList.add_to_end(data)

    print('Items in the list now...')
    linkedList.travese_from_start()
    print('------------------------')
