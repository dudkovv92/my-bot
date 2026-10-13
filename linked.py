class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def length(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count
    def __init__(self):
        self.head = None

    def add(self, value):
        new = Node(value)
        if not self.head:
            self.head = new
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    def show(self):
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next

lst = LinkedList()
lst.add(1)
lst.add(2)
lst.add(3)
lst.show()
print(lst.length())