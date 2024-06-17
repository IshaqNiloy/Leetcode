import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        try:
            square_root = num ** 0.5
            logger.info(f'square root of {num} is {square_root}')
            if square_root == int(square_root):
                return True
            return False

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.isPerfectSquare(9))
