# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val > q.val:
            p, q = q, p

        if p.val <= root.val <= q.val:
            return root
        elif root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)

    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print("{0}".format(node.val))
        self.inorder(node.right)



node6 = TreeNode(6)
node2 = TreeNode(2)
node8 = TreeNode(8)
node0 = TreeNode(0)
node4 = TreeNode(4)
node7 = TreeNode(7)
node9 = TreeNode(9)
node3 = TreeNode(3)
node5 = TreeNode(5)

root = node6

node6.left  = node2
node6.right = node8
node2.left  = node0
node2.right = node4
node8.left  = node7
node8.right = node9
node4.left  = node3
node4.right = node5

s = Solution()
s.inorder(root)

print("-------")

x = s.lowestCommonAncestor(root, node0, node6)
print(x.val)

x = s.lowestCommonAncestor(root, node6, node0)
print(x.val)
