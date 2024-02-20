class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        seen = ''
        sub_string_length_mapping = dict()

        # If the string is empty
        if len(s) == 0:
            return 0

        # If the string has only one character
        elif len(s) == 1:
            return 1

        # If the string has only unique characters
        elif len(set(s)) == len(s):
            max = len(s)
            return max

        # If the string has repeating characters
        else:
            for char in s:
                if char not in seen:
                    seen += char
                else:
                    sub_string_length_mapping[seen] = len(seen)
                    seen = ''
            return max


if __name__ == '__main__':
    obj = Solution()
    result = obj.lengthOfLongestSubstring('abcabcbb')

    print(result)

