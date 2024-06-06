import logging
from collections import Counter

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_dict, word2_dict = dict(), dict()
        try:
            # words have to be of the same length and there shouldn't be any unique character
            if len(word1) != len(word2) or set(list(word1)) != set(list(word2)):
                return False

            # if the lists of frequencies are same then the two strings are close.
            word1_dict = Counter(word1)
            word2_dict = Counter(word2)

            logger.info(f'word1 dict: {word1_dict}')
            logger.info(f'word2 dict: {word2_dict}')

            if sorted(word1_dict.values()) != sorted(word2_dict.values()):
                return False

            return True
        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.closeStrings('abbzzca', 'babzzcz'))
