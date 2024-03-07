# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_linked_list_stack(self, head: Optional[ListNode]) -> List:
        linked_list_stack = list()
        while head:
            linked_list_stack.append(head)
            head = head.next

        return linked_list_stack

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        linked_list_stack = self.get_linked_list_stack(head)
        length_of_linked_list = len(linked_list_stack)

        if length_of_linked_list % 2 == 0:
            return linked_list_stack[int(length_of_linked_list / 2)]
        else:
            return linked_list_stack[int(length_of_linked_list / 2)]



if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    obj = Solution()
    result = obj.middleNode(head=head)

    print(result[0].val)
