import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # sliding window technique
        left, max_length, zero_counter = 0, 0, 0

        try:
            for right in range(len(nums)):
                if nums[right] == 0:
                    zero_counter += 1

                while zero_counter > 1:
                    if nums[left] == 0:
                        zero_counter -= 1
                    left += 1

                max_length = max(max_length, right - left + 1)

            return max_length - 1

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(f'result: {s.longestSubarray(nums=[1,1,1])}')
