import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()
        stack.append(asteroids[0])

        try:
            for i in range(1, len(asteroids)):
                curr = asteroids[i]
                while stack:
                    stack_last_item = stack.pop()
                    logger.info(f'popped item: {stack_last_item}')
                    if (stack_last_item > 0 > curr) or (stack_last_item < 0 < curr):
                        if abs(stack_last_item) >= abs(curr):
                            curr = stack_last_item
                    else:
                        stack.append(stack_last_item)
                        stack.append(curr)
                        break
                if not stack:

                logger.info(f'stack: {stack}')

            return stack
        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.asteroidCollision([10,2,-5]))
