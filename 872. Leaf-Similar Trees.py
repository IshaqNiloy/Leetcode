from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.similar_leaves_tree1 = []
        self.similar_leaves_tree2 = []
        self.counter = 0

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            if self.counter == 1 and root.right is None and root.left is None:
                self.similar_leaves_tree1.append(root.val)
            if self.counter == 2 and root.right is None and root.left is None:
                self.similar_leaves_tree2.append(root.val)

            self.inorder_traversal(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        for root_tuple in [root1, root2]:
            self.counter += 1
            self.inorder_traversal(root_tuple)

        if self.similar_leaves_tree1 == self.similar_leaves_tree2:
            return True

        return False


if __name__ == '__main__':
    # first tree
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)

    # second tree
    root2 = TreeNode(3)
    root2.left = TreeNode(5)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(2)
    root2.right.right.left = TreeNode(9)
    root2.right.right.right = TreeNode(8)

    obj = Solution()
    result = obj.leafSimilar(root1, root2)

    print(result)

