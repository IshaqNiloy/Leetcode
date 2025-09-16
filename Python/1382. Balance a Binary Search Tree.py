import logging

from typing import List, Union

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
    def __init__(self):
        self.sorted_nodes = list()

    def inorder(self, root: TreeNode) -> Union[List[int], None]:

        if not root:
            return

        self.inorder(root.left)
        self.sorted_nodes.append(root.val)
        self.inorder(root.right)

        return self.sorted_nodes

    def create_balanced_BST(self, sorted_nodes: List[int]) -> Union[TreeNode, None]:
        # divide and conquer approach
        if not sorted_nodes:
            return None

        mid = len(sorted_nodes) // 2
        root = TreeNode(sorted_nodes[mid])

        root.left = self.create_balanced_BST(sorted_nodes[:mid])
        root.right = self.create_balanced_BST(sorted_nodes[mid+1:])

        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        try:
            # inorder traversal for sorting
            sorted_inorder = self.inorder(root=root)
            logger.info(f'sorted nodes: {sorted_inorder}')

            # create balanced BST
            root = self.create_balanced_BST(sorted_nodes=sorted_inorder)

            return root

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    s = Solution()
    logger.info(s.balanceBST(root=root).right.val)
