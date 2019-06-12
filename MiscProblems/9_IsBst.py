

class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None
        self.range = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, v):

        new_node = Node(v)
        if self.root == None:
            self.root = new_node
            return

        current_node = self.root

        while True:
            if new_node.v <= current_node.v:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right


    def display_inorder(self, node):

        if node.left is not None:
            self.display_inorder(node.left)

        print("{0} {1}".format(node.v, node.range))

        if node.right is not None:
            self.display_inorder(node.right)


    def is_bst(self, node):

        if node is None:
            return True

        if node.left is None and node.right is None:
            node.range = [node.v, node.v]
            return True

        if self.is_bst(node.left) and self.is_bst(node.right):
            node.range = [node.v, node.v]

            if node.left is not None:
                lc_range = node.left.range
                if lc_range[1] > node.v:
                    return False
                else:
                    node.range[0] = lc_range[0]

            if node.right is not None:
                rc_range = node.right.range
                if rc_range[0] <= node.v:
                    return False
                else:
                    node.range[1] = rc_range[1]

            return True
        else:
            return False

bst = BST()

# Create the tree given in the above diagram
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);
bst.insert(14);

print(bst.is_bst(bst.root))
bst.display_inorder(bst.root)

node100 = Node(100)
node50 = Node(50)
node150 = Node(150)
node120 = Node(120)
node110 = Node(110)
node140 = Node(140)
node70 = Node(70)
node149 = Node(149)

node100.left = node50
node100.right = node150
node150.left = node120
node120.left = node110
node120.right = node140
node140.left = node70
node140.right = node149

print(bst.is_bst(node100))
bst.display_inorder(node100)



