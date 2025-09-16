import logging

from typing import List, Optional

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
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head.next.next:
            return [-1, -1]
        prev, current, next = head, head.next, head.next.next
        first_critical_point, last_critical_point, position = 0, 0, 2
        first_adjacent_point, second_adjacent_point = 0, 0,
        min_distance, max_distance = float('inf'), float('-inf')

        try:
            while next:
                execute_next = False
                if prev.val > current.val < next.val or prev.val < current.val > next.val:
                    # first critical point
                    if not first_critical_point:
                        first_critical_point = position
                    # last critical point
                    last_critical_point = position

                    # first adjacent point
                    if not first_adjacent_point:
                        first_adjacent_point = position
                        execute_next = True

                    # second adjacent point
                    if first_adjacent_point and not execute_next:
                        second_adjacent_point = position
                        # min distance
                        min_distance = min(min_distance, second_adjacent_point - first_adjacent_point)
                        first_adjacent_point = second_adjacent_point

                prev, current, next = current, next, next.next
                position += 1

            logger.info(f'first adjacent point: {first_adjacent_point}')
            logger.info(f'second adjacent point: {second_adjacent_point}')

            logger.info(f'first critical point: {first_critical_point}')
            logger.info(f'last critical point: {last_critical_point}')

            max_distance = last_critical_point - first_critical_point

            if max_distance:
                return [min_distance, max_distance]
            return [-1, -1]
        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    head = ListNode(val=5)
    node1 = ListNode(val=3)
    head.next = node1
    node2 = ListNode(val=1)
    node1.next = node2
    node3 = ListNode(val=2)
    node2.next = node3
    node4 = ListNode(val=5)
    node3.next = node4
    node5 = ListNode(val=1)
    node4.next = node5
    node6 = ListNode(val=2)
    node5.next = node6
    node6 = None

    s = Solution()
    logger.info(s.nodesBetweenCriticalPoints(head=head))
