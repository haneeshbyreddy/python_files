class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
 
class BinaryTree:
    def create(self):
        value = int(input("Enter the value (-1 for no node): "))
        if value == -1:
            return None
        new_node = Node(value)
        print("Enter the value of left child")
        new_node.left = self.create()
        print("Enter the value of right child")
        new_node.right = self.create()
        return new_node
 
    def inorder_display(self, node):
        if node is not None:
            self.inorder_display(node.left)
            print(node.value, end=' ')
            self.inorder_display(node.right)
    def postorder_display(self,node):
        if node is not None:
            self.postorder_display(node.left)
            self.postorder_display(node.right)
            print(node.value)
    def preorder_display(self,node):
        if node is not None:
            print(node.value)
            self.preorder_display(node.left)
            self.preorder_display(node.right)
           
       
 
# Create and use the binary tree
tree = BinaryTree()
root = tree.create()
print("In-order traversal of the tree:")
tree.inorder_display(root)
print("post-order traversal of the tree:")
tree.postorder_display(root)
 
print("pre-order traversal of the tree:")
tree.preorder_display(root)
 