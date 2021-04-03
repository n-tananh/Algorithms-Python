# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printPreorder(root):
    if root:
        print(root.val, end=' ')

        printPreorder(root.left)

        printPreorder(root.right)

def isSameTree(p, q):
    if p is None or q is None:
        return p is q

    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)


    n1.left = n2
    n1.right = n3


    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)

    l1.left = l2
    l1.right = l3

    printPreorder(n1)
    print()
    printPreorder(l1)

    print(isSameTree(n1, l1))
