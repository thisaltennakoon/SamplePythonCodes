class Node:
    next = None
    def __init__(self, value):
        self.value = value

    def set_next(self, nextNode):
        self.next = nextNode

class LinkedList():

    first = None
    last = None

    def addLast(self, item):
        node = Node(item)
        if self.first==None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def addFirst(self, item):
        node = Node(item)
        if self.first == None:
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node

    def removeFirst(self):
        if self.first == None:
            return
        elif self.first == self.last:
            self.first = None
            self.last = None
        else:
            second = self.first.next
            self.first.next = None
            self.first = second

    def removeLast(self):
        if self.first == None:
            return
        elif self.first == self.last:
            self.first = None
            self.last = None
        else:
            current = self.first
            previous_node = None
            while current.next!=None:
                previous_node  = current
                current = current.next
            previous_node.next = None
            self.last = previous_node

    def indexOf(self, item):
        index = 0
        current = self.first
        while current != None:
            if current.value == item:
                return index
            current = current.next
            index = index+1
        return -1

    def contains(self, item):
        return self.indexOf(item) != -1

    def print_list(self):
        current = self.first
        while current!=None:
            print(current.value)
            current = current.next


linked_list = LinkedList()
linked_list.addLast(10)
#linked_list.addLast(20)
#linked_list.addLast(30)
#linked_list.addFirst(5)
linked_list.print_list()
linked_list.removeFirst()
linked_list.removeLast()
linked_list.print_list()
#print(linked_list.indexOf(300))
#print(linked_list.contains(40))