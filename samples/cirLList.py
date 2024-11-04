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
        else:
            self._addMore(self.root, data)

    def _addMore(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._addMore(current_node.left, data)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._addMore(current_node.right, data)
        else:
            # Duplicate values are not allowed in this example
            print(f"Value {data} already exists in the tree.")

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, current_node):
        if current_node:
            self._inorder(current_node.left)
            if (current_node == self.root):
                print(current_node.data, "\troot")
            else:
                print(current_node.data)
            self._inorder(current_node.right)
        else:
            return

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, current_node):
        if current_node:
            if (current_node == self.root):
                print(current_node.data, "\troot")
            else:
                print(current_node.data)
            self._preorder(current_node.left)
            self._preorder(current_node.right)
        else:
            return

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, current_node):
        if current_node:
            self._postorder(current_node.left)
            self._postorder(current_node.right)

            if (current_node == self.root):
                print(current_node.data, "\troot")
            else:
                print(current_node.data)
        else:
            return

    def search(self, data):
        if self.root:
            self._search(self.root, data)
        else:
            print("tree is empty")

    def _search(self, currentnode, data):
        if currentnode:
            if data == currentnode.data:
                print("data found\t" + str(data))
                return
            if data < currentnode.data:
                self._search(currentnode.left, data)
            else:
                self._search(currentnode.right, data)
        else:
            print("Not found\t" + str(data))


# Create a binary tree instance
binary_tree = BinaryTree()

# Insert nodes
binary_tree.add(30)
binary_tree.add(28)
binary_tree.add(40)
binary_tree.add(20)
binary_tree.add(10)
binary_tree.add(25)
binary_tree.add(5)
binary_tree.add(22)
binary_tree.add(27)
binary_tree.add(38)
binary_tree.add(45)
binary_tree.add(23)

# Perform inorder traversal
print("Inorder Traversal:")
binary_tree.inorder()

print("**********************************************")
print("Preorder Traversal:")
binary_tree.preorder()

print("**********************************************")
print("Postorder Traversal:")
binary_tree.postorder()
print("*******************************")
# binary_tree.search(27)
# binary_tree.search(19)
