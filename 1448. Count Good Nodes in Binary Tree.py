import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        


if __name__ == '__main__':
    root = TreeNode(val=4)
    node2 = TreeNode(val=2)
    node1 = TreeNode(val=1)
    node3 = TreeNode(val=3)
    node7 = TreeNode(val=7)

    root.left = node2
    root.right = node7
    node2.left = node1
    node2.right = node3

    s = Solution()
    logger.info(s.goodNodes(root=root))


