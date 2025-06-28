class Node:
    def __init__(self,data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

    def add(self,data,parentdata=None):
        node = Node(data)

        if self.root == None:
            self.root = node
            return

        parent=self.findnode(parentdata,self.root)

        if parent == None:
            print("parent not found")
            return

        parent.children.append(node)

    def findnode(self,data,node):
        if node.data == data:
            return node

        for child in node.children:
            nodefound = self.findnode(data,child)
            if nodefound != None:
                return nodefound

        return None

    def display(self,depth=0,node=None):
        if not node:
            node = self.root

        print(" "*depth,node.data)

        for child in node.children:
            self.display(depth+1,child)

    def remove(self,data):
        if not self.root:
            print("root is empty")
            return

        if self.root == data:
            self.root = None
            return

        parent=self.findparent(data,data,node)

    def findparent(self,data,node=None):
        if not node:
            node = self.root  