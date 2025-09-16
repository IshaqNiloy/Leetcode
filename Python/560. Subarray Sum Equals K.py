import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum, prefix_sum_index_mapping = 0, 

        try:
            for num in nums:
                prefix_sum += num

        except Exception as e:
            logger.error(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.subarraySum([1,1,1], 2))

