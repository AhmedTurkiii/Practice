# Node Class:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    


class LinkedList:
    def __init__(self):
        self.head = None

    def addNodetoFront(self, value):

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def addNodetoEnd(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        if not self.head:
            return "Empty List"
        else:
            current = self.head
            while current:
                print(current.data, end=" --> ")
                current = current.next
            print("None")

    def reverse_List(self):
        current = self.head
        prev = None

        if self.head is None:
            return "list is empty"
        else:
            while current:
                temp = current.next
                
            
            


list1 = LinkedList()

list1.addNodetoFront(1)
list1.addNodetoEnd(2)
list1.addNodetoEnd(3)
list1.print_list()