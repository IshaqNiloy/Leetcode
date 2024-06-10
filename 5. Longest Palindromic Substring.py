import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    @staticmethod
    def get_longest_palindromic_sub_string(s, i, left_pointer: int, right_pointer: int) -> str:
        result = ''
        while left_pointer >= 0 and right_pointer < len(s) and s[left_pointer] == s[right_pointer]:
            result = s[left_pointer:i] + s[i:right_pointer + 1]
            left_pointer -= 1
            right_pointer += 1

        return result

    def longestPalindrome(self, s: str) -> str:
        final_result = ''
        left_pointer, right_pointer = 0, 0

        # edge cases
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            return s[0]

        for i in range(len(s)):
            # for odd number of characters in the string
            if len(s) % 2 != 0:
                result = self.get_longest_palindromic_sub_string(s, i, left_pointer, right_pointer)
            # for even number of characters in the string
            else:
                if i < len(s) - 1 and s[i] == s[i+1]:
                    left_pointer = i - 1
                    right_pointer = i + 2
                    result = self.get_longest_palindromic_sub_string(s, i, left_pointer, right_pointer)
                    if result == '':
                        result = s[i] + s[i + 1]
                else:
                    continue

            if len(result) > len(final_result):
                final_result = result

            left_pointer = i - 1
            right_pointer = i + 1

        return final_result


if __name__ == '__main__':
    s = Solution()
    logger.info(s.longestPalindrome('cbbd'))
