import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = 0
        prefix_sum_list = [0]

        try:
            for item in gain:
                prefix_sum += item
                prefix_sum_list.append(prefix_sum)
            logger.info(f'prefix sum list: {prefix_sum_list}')

            return max(prefix_sum_list)
        except Exception as e:
            logger.info(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.largestAltitude([-4,-3,-2,-1,4,3,2]))