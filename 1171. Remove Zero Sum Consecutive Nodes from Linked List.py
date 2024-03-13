# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix_sum_mapping = dict()
        current = head
        previous = ListNode(val=0, next=head)
        prefix_sum_mapping[0] = previous
        prefix_sum = 0

        while current:
            prefix_sum = prefix_sum + current.val

            if prefix_sum not in prefix_sum_mapping:
                prefix_sum_mapping[prefix_sum] = current
            else:
                prefix_sum_mapping[prefix_sum].next = current.next

            current = current.next
        print(prefix_sum_mapping)
        return prefix_sum_mapping[0].next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(5)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(-5)
    head.next.next.next.next = ListNode(1)

    obj = Solution()
    result = obj.removeZeroSumSublists(head=head)

    print(result.val)
