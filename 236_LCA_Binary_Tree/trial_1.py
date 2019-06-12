# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.find_path(root, p)
        q_path = self.find_path(root, q)

        i = 0
        min_path = min(len(p_path), len(q_path))

        while i < min_path and p_path[i] == q_path[i]:
            i += 1

        return p_path[i-1]


    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print("{0}".format(node.val))
        self.inorder(node.right)

    def find_path(self, root, node):
        if root is None:
            return []

        if root == node:
            return [node]

        left_path = self.find_path(root.left, node)
        if len(left_path) > 0:
            return [root] + left_path

        right_path = self.find_path(root.right, node)
        if len(right_path) > 0:
            return [root] + right_path

        return []


node3 = TreeNode(3)
node5 = TreeNode(5)
node1 = TreeNode(1)
node6 = TreeNode(6)
node2 = TreeNode(2)
node0 = TreeNode(0)
node8 = TreeNode(8)
node7 = TreeNode(7)
node4 = TreeNode(4)


root = node3

node3.left = node5
node3.right = node1
node5.left = node6
node5.right = node2
node1.left = node0
node1.right = node8
node2.left = node7
node2.right = node4

s = Solution()
s.inorder(root)

node7_path = s.find_path(root, node7)
for n in node7_path:
    print(n.val),

print("--------")

lca_node = s.lowestCommonAncestor(root, node7, node4)
print(lca_node.val)

lca_node = s.lowestCommonAncestor(root, node4, node7)
print(lca_node.val)