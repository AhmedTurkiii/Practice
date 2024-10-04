# LinkedList
class Node:
    def __init__(self, data):  # Corrected constructor with two underscores
        self.data = data       # Store data in the node
        self.next = None  
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_AtFront(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def insert_AtEnd(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print_list(self):
        if self.head is None:
            print("Empty List")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" --> ")  # Print the node data
                temp = temp.next
            print("None")
    
    def search_list(self,value):
        # if self.head is None:
        #     return False
        # else:
        temp = self.head

        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False

    def reverse_list(self):

        return

list1 = LinkedList()
list1.insert_AtEnd(1)
list1.insert_AtEnd(2)
list1.insert_AtEnd(3)
list1.insert_AtFront(5)
list2 = LinkedList()

print(list1.search_list(7))
print(list2.search_list(5))

list1.print_list()