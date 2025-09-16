import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def removeStars(self, s: str) -> str:
        stack = list()

        try:
            for char in s:
                if char != '*':
                    stack.append(char)
                if char == '*':
                    stack.pop()

            return ''.join(stack)
        except Exception as e:
            logger.error(f'exception: {e}')


if __name__ == '__main__':
    test = Solution()
    logger.info(test.removeStars('erase*****'))

