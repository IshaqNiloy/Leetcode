import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def method(self):
        logger.info(f'working....')


if __name__ == '__main__':
    obj = Solution()
    logger.info(obj.method())
