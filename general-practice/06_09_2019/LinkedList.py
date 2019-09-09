class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.start_node = Node("||START||")

    def add_to_start(self, item):
        node = Node(item)
        node.next = self.start_node.next
        self.start_node.next = node
    
    def add_to_last(self, item):
        node = Node(item)
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.next = node
    
    def remove_from_start(self):
        if self.start_node.next is None:
            print('List is empty. Nothing to delete')
        else:
            node = self.start_node.next
            self.start_node.next = node.next
            node = None
        
    def remove_from_end(self):
        if self.start_node.next is None:
            print('List is empty. Nothing to delete')
        else:
            node = self.start_node
            while node.next.next is not None:
                node = node.next
            
            node.next = None
        
    def travese_list(self):
        print("=======")
        if self.start_node.next is None:
            print('List is empty')
        else:
            node = self.start_node.next
            while node is not None:
                print(node.item)
                node = node.next

    def count(self):
        c = 0
        node = self.start_node.next
        while node is not None:
            c += 1
            node = node.next
        return c

if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.travese_list()
    linkedList.add_to_start(5)
    linkedList.add_to_start(7)
    linkedList.add_to_start(17)
    linkedList.travese_list()
    print('Total items = {}'.format(linkedList.count()))
    linkedList.add_to_start(7)
    linkedList.travese_list()
    print('Total items = {}'.format(linkedList.count()))
    linkedList.remove_from_start()
    linkedList.remove_from_end()
    linkedList.travese_list()
    print('Total items = {}'.format(linkedList.count()))