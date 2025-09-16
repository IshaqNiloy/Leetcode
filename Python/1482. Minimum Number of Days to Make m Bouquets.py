import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def find_min_max(bloom_day: List[int]) -> List[int]:
            min_value, max_value = 10 ** 9, 0

            for item in bloom_day:
                min_value = min(min_value, item)
                max_value = max(max_value, item)

            return [min_value, max_value]

        try:
            min_value, max_value = find_min_max(bloom_day=bloomDay)
            logger.info(f'minimum value: {min_value}, maximum value: {max_value}')

            

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))
