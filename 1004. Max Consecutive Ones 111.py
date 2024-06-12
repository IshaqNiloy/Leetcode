from typing import List
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window technique
        start, max_length, zero_counter = 0, 0, 0
        try:
            for end in range(len(nums)):
                if nums[end] == 0:
                    zero_counter += 1

                while zero_counter > k:
                    if nums[start] == 0:
                        zero_counter -= 1
                    start += 1

                max_length = max(max_length, end - start + 1)
            return max_length

        except Exception as e:
            logger.info(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(f'result: {s.longestOnes(nums=[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k=3)}')
