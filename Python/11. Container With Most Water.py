import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers approach
        max_area, left_pointer, right_pointer = 0, 0, len(height) - 1

        try:
            while left_pointer < right_pointer:
                max_area = max(max_area, min(height[right_pointer], height[left_pointer]) * (right_pointer - left_pointer))

                if height[left_pointer] < height[right_pointer]:
                    left_pointer += 1
                else:
                    right_pointer -= 1

            return max_area

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.maxArea([1, 2]))
