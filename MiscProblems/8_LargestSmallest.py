# Given a root of a Binary Search Tree (BST) and a number num,
# implement an efficient function findLargestSmallerKey
# that finds the largest key in the tree that is smaller than num.
#
# If such a number doesn’t exist, return -1.
# Assume that all keys in the tree are nonnegative.

# A node
class Node:
    # Constructor to create a new node
    def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None
      self.parent = None

# A binary search tree
class BinarySearchTree:

    # Constructor to create a new BST
    def __init__(self):
      self.root = None

    def find_largest_smaller_key(self, num):
        # your code goes here
        #        100
        #     50      150
        # 20
        #
        # t - root
        #
        # t is none (-1)
        # num <= t (recurse left subtree)
        #
        # num > t
        # - t.right is none (t)
        # - t.right >= num (t)
        # - t.right < num (recurse right subtree)

        t = self.root

        if t is None:
            return -1

        if t.key >= num:
            self.root = t.left
            return self.find_largest_smaller_key(num)
        elif t.key < num:
            if t.right is None or t.right.key >= num:
                return t.key
            elif t.right.key < num:
                self.root = t.right
                return self.find_largest_smaller_key(num)


    # Given a binary search tree and a number, inserts a
    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use(the standard trick to avoid
    # using reference parameters)
    def insert(self, key):

        # 1) If tree is empty, create the root
        if (self.root is None):
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)

        while (currentNode is not None):
            if (key < currentNode.key):
                if (currentNode.left is None):
                    currentNode.left = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.left
            else:
                if (currentNode.right is None):
                    currentNode.right = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.right


#########################################
# Driver program to test above function #
#########################################

bst = BinarySearchTree()

# Create the tree given in the above diagram
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);
bst.insert(14);

result = bst.find_largest_smaller_key(23)

print("Largest smaller number is %d " % (result))