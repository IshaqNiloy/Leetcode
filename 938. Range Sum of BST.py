from typing import Optional, Union

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.total = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            self.rangeSumBST(root.left, low, high)
            if low <= root.val <= high:
                self.total += root.val
            self.rangeSumBST(root.right, low, high)

        return self.total


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(13)
    root.right.right = TreeNode(18)

    obj = Solution()
    result = obj.rangeSumBST(root, 7, 15)

    print(result)