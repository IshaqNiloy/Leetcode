import logging
import math
from typing import Optional

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = list()
        current_node = head
        try:
            # converts the linked list to a stack
            while current_node:
                stack.append(current_node)
                current_node = current_node.next

            if len(stack) == 1:
                return None

            # finds the index of the middle node
            middle_node_index = math.floor(len(stack) / 2)
            logger.info(f'middle_node_index: {middle_node_index}')

            current_node = head
            i = 0
            while i < middle_node_index:
                if i == middle_node_index - 1:
                    current_node.next = current_node.next.next
                current_node = current_node.next
                i += 1

            return head
        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    head = ListNode(val=1)
    node2 = ListNode(val=2)
    node3 = ListNode(val=3)
    node4 = ListNode(val=4)
    node5 = ListNode(val=7)
    node6 = ListNode(val=1)
    node7 = ListNode(val=2)
    node8 = ListNode(val=6)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8

    s = Solution()
    logger.info(s.deleteMiddle(head=head).next.next.next.next.val)

