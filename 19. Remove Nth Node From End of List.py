from typing import List, Optional

from main import ListNode


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def find_the_length(head: Optional[ListNode]) -> int:
        length = 0
        while head:
            length += 1
            head = head.next

        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        linked_list_length = self.find_the_length(head=head)
        current = head
        if n == 1 and linked_list_length == 1:
            return None
        for i in range(0, (linked_list_length - n)):
            if i != (linked_list_length - n) - 1:
                head = head.next
        print(head.next)
        if head.next:
            head.next = head.next.next

        return current


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    obj = Solution()
    result = obj.removeNthFromEnd(head=head, n=2)

    print(result.next.next.next.val)
