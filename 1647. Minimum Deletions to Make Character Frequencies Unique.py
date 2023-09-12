class Solution:
    def minDeletions(self, s: str) -> dict:
        char_dict = {}

        for i in range(len(s)):
            if not char_dict.get(s[i]):
                char_dict[s[i]] = 1
            else:
                char_dict[s[i]] += 1
        # return char_dict

        for val in char_dict.values():
            if val == 1:
                continue
            if val in char_dict.values():

if __name__ == '__main__':
    obj = Solution()
    result = obj.minDeletions('aaabbbcc')

    print(result)
