class BinNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)
    def isLeaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False

class BinarySearchTree(object):
    def __init__(self, root = None):
        self.root = root
        self.string = str(self.root)
    def insert(self, data):
        if self.root is None:
            self.root = BinNode(data)
            self.string = str(self.root)
            return
        current = self.root
        previous = None
        switch = None
        while current:
            previous = current
            if current.data <= data:
                current = current.right
                switch = 1
            else:
                current = current.left
                switch = 0
        new_node = BinNode(data)
        if switch == 0:
            previous.left = new_node
        if switch == 1:
            previous.right = new_node
    def preorderPrint(self):
        if self.root:
            print(self.root)
        else:
            return
        BinarySearchTree(self.root.left).preorderPrint()
        BinarySearchTree(self.root.right).preorderPrint()
    def preorder__str__(self):
        self.string = str(self.root)
        if self.root is None:
            return ''
        self.string += '('+BinarySearchTree(self.root.left).preorder__str__()+')'
        self.string += '['+BinarySearchTree(self.root.right).preorder__str__()+']'
        return self.string