## 1. Introduction ##

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    # Add `insert` method here.
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value=value)
        elif not self.root.left:
            self.root.left = Node(value=value)
        elif not self.root.right:
            self.root.right = Node(value=value)

tree = BinaryTree(Node(value=1))
tree.insert(2)
tree.insert(3)
tree.insert(4)
root = tree.root.value
left = tree.root.left.value
right = tree.root.right.value

## 2. Multiple Inserts ##

level_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        # Helpful method to keep track of Node values.
        return "<Node: {}>".format(self.value)    

class BinaryTree:
    def __init__(self, values=None):
        self.root = None
        if values:
            self.insert(values)
    
    # Implement your `insert` method here.
level_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "<Node: {}>".format(self.value)

class BinaryTree:
    def __init__(self, values=None):
        self.root = None
        if values:
            self.insert(values)
    
    def insert(self, values, index=0):
        node = None
        if index < len(values):
            node = Node(value=values[index])
            if not self.root:
                self.root = node
            node.left = self.insert(values, index=index*2+1)
            node.right = self.insert(values, index=index*2+2)
            
        return node

tree = BinaryTree(level_order)
root = tree.root.value
child = tree.root.left.right.left.value

## 3. Interior, Child, and Parent Nodes ##

level_order = [1, 2, 3, 4, 5]

class BinaryTree(BaseBinaryTree):
    pass  # no-op method that let's us declare our tree.
    # Your methods go here.
    
tree = BinaryTree(level_order)

# Uncomment the following to test.
#root_parent = tree.is_parent(tree.root)
#parent = tree.is_parent(tree.root.left)
#interior = tree.is_interior(tree.root.left)
#root_leaf = tree.is_leaf(tree.root)
#leaf = tree.is_leaf(tree.root.left.left)
level_order = [1, 2, 3, 4, 5]

class BinaryTree(BaseBinaryTree):
    def is_parent(self, node):
        return bool(node.left or node.right)
    
    def is_interior(self, node):
        return (not node == self.root) and self.is_parent(node)
    
    def is_leaf(self, node):
        return (not node == self.root) and not self.is_interior(node)

tree = BinaryTree(level_order)
root_parent = tree.is_parent(tree.root)
parent = tree.is_parent(tree.root.left)
interior = tree.is_interior(tree.root.left)
root_leaf = tree.is_leaf(tree.root)
leaf = tree.is_leaf(tree.root.left.left)

## 4. Traversing the Tree ##

level_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class BinaryTree(BaseBinaryTree):
    pass
    # Add your traversal methods here.
    
tree = BinaryTree(level_order)
# Assign the variables here.
level_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class BinaryTree(BaseBinaryTree):
    def preorder_traverse(self, node):
        if not node:
            return []
        return (
            [node.value] +
            self.preorder_traverse(node.left) +
            self.preorder_traverse(node.right)
        )
    
    def inorder_traverse(self, node):
        if not node:
            return []
        return (
            self.preorder_traverse(node.left) +
            [node.value] +
            self.preorder_traverse(node.right)
        )
    
    def postorder_traverse(self, node):
        if not node:
            return []
        return (
            self.postorder_traverse(node.left) +
            self.postorder_traverse(node.right) +
            [node.value]
        )

tree = BinaryTree(level_order)
preorder = tree.preorder_traverse(tree.root)
inorder = tree.inorder_traverse(tree.root)
postorder = tree.postorder_traverse(tree.root)

## 5. Finding Total Nodes and Depth ##

class BinaryTree(BaseBinaryTree):
    pass
    # Add the new methods here.
    
tree = BinaryTree(level_order)
# Assign the variables here.
class BinaryTree(BaseBinaryTree):
    def depth(self, node):
        if not node:
            return 0
        return max(self.depth(node.left), self.depth(node.right)) + 1
    
    def num_nodes(self, node):
        return len(self.preorder_traverse(node))
    
# Level Order list is provided for you
tree = BinaryTree(level_order)
depth = tree.depth(tree.root)
num_nodes = tree.num_nodes(tree.root)

## 6. Types of Trees ##

class BinaryTree(BaseBinaryTree):
    pass
    # Add `is_balanced` method here.
    
# Level Order list is provided for you
tree = BinaryTree(level_order)
class BinaryTree(BaseBinaryTree):
    def is_balanced(self, node):
        if not node:
            return True
        
        left_height = self.depth(node.left)
        right_height = self.depth(node.right)
        
        if (abs(right_height - left_height) <= 1
               and self.is_balanced(node.left)
               and self.is_balanced(node.right)):
            return True
        return False
    
    
# Level Order list is provided for you
tree = BinaryTree(level_order)
balanced = tree.is_balanced(tree.root)