from typing import List, Optional
from main import ListNode


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_stack = []

        while head:
            node_stack.append(head)
            head = head.next

        # if the linked list has only one node
        if n == 1 and len(node_stack) == 1:
            return None

        # if head is asked to be deleted
        if n == len(node_stack):
            return node_stack[1]

        deleted_node = None
        for i in range(0, n):
            deleted_node = node_stack.pop()

        node_before_deleted_node = node_stack.pop()
        node_before_deleted_node.next = deleted_node.next

        # if the list becomes empty then the last item that has been deleted is the head of the linked list
        if not len(node_stack):
            return node_before_deleted_node

        # returns the first item of the list which is the head
        return node_stack[0]


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    obj = Solution()
    result = obj.removeNthFromEnd(head=head, n=2)

    print(result.next.next.next.val)
