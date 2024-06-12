class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # max = 0
        # seen = ''
        # sub_string_length_mapping = dict()
        #
        # # If the string is empty
        # if len(s) == 0:
        #     return 0
        #
        # # If the string has only one character
        # elif len(s) == 1:
        #     return 1
        #
        # # If the string has only unique characters
        # elif len(set(s)) == len(s):
        #     max = len(s)
        #     return max
        #
        # # If the string has repeating characters
        # else:
        #     for char in s:
        #         if char not in seen:
        #             seen += char
        #         else:
        #             sub_string_length_mapping[seen] = len(seen)
        #             seen = ''
        #     return max

        # sliding window technique

        start, character_index_mapping, max_length = 0, dict(), 0

        try:
            for end in range(len(s)):
                if s[end] in character_index_mapping and character_index_mapping[s[end]] >= start:
                    start = character_index_mapping[s[end]] + 1

                character_index_mapping[s[end]] = end
                max_length = max(max_length, end - start + 1)

            return max_length

        except Exception as e:
            print(f'exception: {e}')


if __name__ == '__main__':
    obj = Solution()
    result = obj.lengthOfLongestSubstring('abba')

    print(result)

