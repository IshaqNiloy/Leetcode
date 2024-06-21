import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left_pointer = 0
        window, max_window = 0, 0
        satisfied = 0

        try:
            for right_pointer in range(len(customers)):
                if grumpy[right_pointer]:
                    window += customers[right_pointer]
                else:
                    satisfied += customers[right_pointer]

                if right_pointer - left_pointer + 1 > minutes:
                    if grumpy[left_pointer]:
                        window -= customers[left_pointer]
                    left_pointer += 1

                max_window = max(max_window, window)

            return satisfied + max_window

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.maxSatisfied(customers = [4,10,10], grumpy = [1,1,0], minutes = 2))
