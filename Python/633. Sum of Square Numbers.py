import logging
import math

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        try:
            if c == 0:
                return True

            for b in range(c):
                if b ** 2 <= c:
                    a = math.sqrt(c - b ** 2)
                    if int(a) == a:
                        return True
                else:
                    break

            return False
        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.judgeSquareSum(0))
