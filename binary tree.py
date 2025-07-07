class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        self.recuradd(data, self.root)

    def recuradd(self, data, node):
        if node.left is None:
            node.left = Node(data)
        elif node.right is None:
            node.right = Node(data)
        else:
            self.recuradd(data, node.left)

    def display(self, node=None, depth=0):
        if node is None:
            node = self.root
            if node is None:  # Handle empty tree
                return

        print("  " * depth + str(node.data))  # Print current node

        # Display left child first (if exists)
        if node.left:
            self.display(node.left, depth + 1)
        # Then display right child (if exists)
        if node.right:
            self.display(node.right, depth + 1)

    def remove(self, data):
        if self.root is None:
            print("Tree is empty")
            return

        if self.root.data == data:
            self.root = None
            return

        self.recurremove(data, self.root)  # Fixed: pass self.root instead of node

    def recurremove(self, data, node):
        if node is None:
            return

        if node.left and node.left.data == data:
            node.left = None
            return
        if node.right and node.right.data == data:
            node.right = None
            return

        self.recurremove(data, node.left)
        self.recurremove(data, node.right)

    def search(self, data):
        nodefound = self.recursivesearch(data, self.root)

        if nodefound:
            print("Node found")
        else:
            print("Node not found")

    def recursivesearch(self, data, node):
        if not node:
            return None
        if node.data == data:
            return node

        left_search = self.recursivesearch(data, node.left)
        if left_search:
            return left_search
        return self.recursivesearch(data, node.right)

def main():
    tree = BinaryTree()

    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.add(10)
    tree.add(11)
    tree.add(12)
    tree.display()

    tree.search(9)
    tree.search(7)

if __name__ == "__main__":
    main()