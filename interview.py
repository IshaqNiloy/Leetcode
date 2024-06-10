import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def reverseString(self, s: list) -> list:
        starting_pointer = 0
        ending_pointer = len(s) - 1

        while starting_pointer != ending_pointer:
            temp = s[starting_pointer]
            s[starting_pointer] = s[ending_pointer]
            s[ending_pointer] = temp
            starting_pointer += 1
            ending_pointer -= 1
            if starting_pointer > ending_pointer:
                break

        return s


if __name__ == '__main__':
    s = Solution()
    logger.info(s.reverseString( ["H","a","n","n","a","h"]))

