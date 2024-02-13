from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        word_stack = list()
        reverse_string = ''

        for word in words:
            for char in word:
                word_stack.append(char)
            for _ in range(len(word_stack)):
                reverse_string += word_stack.pop()
            if word == reverse_string:
                return word
            word_stack.clear()
            reverse_string = ''

        return ''


if __name__ == '__main__':
    obj = Solution()
    result = obj.firstPalindrome(["def", "ghi"])

    print(result)
