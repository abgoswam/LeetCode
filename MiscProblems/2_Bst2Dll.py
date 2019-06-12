class TreeNode():
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None

class BST():
    def insert(self, v, pos):
        if pos is None:
            return TreeNode(v)

        if v <= pos.v:
            pos.left = self.insert(v, pos.left)
        else:
            pos.right = self.insert(v, pos.right)

        return pos

    def display_preorder(self, pos):
        if pos is None:
            return

        self.display_preorder(pos.left)
        print(pos.v)
        self.display_preorder(pos.right)


    def bst_dll(self, pos):
        if pos is None:
            return None

        a = self.bst_dll(pos.left)
        b = self.bst_dll(pos.right)

        if a is not None and b is not None:
            ae = a.left
            be = b.left
            pos.left = ae
            pos.right = b
            ae.right = pos
            b.left = pos
            a.left = be
            be.right = a
            return a

        if a is None and b is not None:
            be = b.left
            pos.right = b
            b.left = pos
            pos.left = be
            be.right = pos
            return pos

        if a is not None and b is None:
            ae = a.left
            pos.left = ae
            ae.right = pos
            a.left = pos
            pos.right = a
            return a

        if a is None and b is None:
            pos.left = pos
            pos.right = pos
            return pos

# nos = [50, 25, 100, 10,40,75,120, 5,15,30,45]
nos = [50, 25, 10]

bst = BST()
head = None
for n in nos:
    head = bst.insert(n, head)

bst.display_preorder(head)
dll_head = bst.bst_dll(head)

a = dll_head
while True and (a is not None):
    print("{0} ".format(a.v))
    if a.right == dll_head:
        break

    a = a.right

