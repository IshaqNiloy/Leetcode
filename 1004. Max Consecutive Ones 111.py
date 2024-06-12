from typing import List
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_index_list, window_size, max_consecutive_ones, j = list(), 0, 0, 1
        try:
            for index, num in enumerate(nums):
                if num == 0:
                    zero_index_list.append(index)
                if num == 0 and k != 0:
                    k -= 1
                elif num == 0 and k == 0:
                    max_consecutive_ones = max(max_consecutive_ones, window_size)
                    window_size = zero_index_list[j] - zero_index_list[j-1]
                    j += 1

                window_size += 1
            logger.info(f'window size: {window_size}')

            return max_consecutive_ones

        except Exception as e:
            logger.info(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(f'result: {s.longestOnes(nums=[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k=3)}')
