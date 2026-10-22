class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def find(self, value):
        cur = self.root
        while cur:
            if value == cur.value:
                return True
            elif value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        return False
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return
        cur = self.root
        while True:
            if value < cur.value:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(value)
                    return
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(value)
                    return

    def show(self, node):
        if node:
            self.show(node.left)
            print(node.value)
            self.show(node.right)

t = Tree()
t.add(5)
t.add(3)
t.add(8)
t.add(1)
t.add(4)
t.show(t.root)
print(t.find(4))
print(t.find(10))