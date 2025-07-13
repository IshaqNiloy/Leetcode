import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)

class Solution:
    def possibleStringCount(self, word: str) -> int:
        # case 1: If word contains only one letter then there will be only one possible string.
        if len(word) == 1:
            return 1
        # case 2: If word contains multiple letters then there can be more than one possible strings.
        total_count = 0
        first_pointer = 0
        second_pointer = 1

        # Sliding window approach
        while first_pointer < len(word) or second_pointer < len(word):
            if word[first_pointer] == word[second_pointer]:
                while word[first_pointer] == word[second_pointer]:
                    second_pointer += 1
                    if second_pointer >= len(word):
                        break
                total_count += second_pointer - first_pointer - 1
                first_pointer = second_pointer
                second_pointer += 1
                if second_pointer >= len(word):
                    break
            else:
                first_pointer += 1
                if second_pointer >= len(word):
                    second_pointer += 1

        return total_count + 1


if __name__ == '__main__':
    obj = Solution()
    print(obj.possibleStringCount('ccr'))
