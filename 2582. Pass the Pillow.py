import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        try:
            if time < n:
                return time + 1

            total_cycles = 2 * n - 2
            effective_time = time % total_cycles
            logger.info(f'effective_time: {effective_time}')
            # moving forward
            if effective_time < n:
                return effective_time + 1
            # moving backwards
            return 2 * n - effective_time - 1
        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.passThePillow(n=4, time=5))
