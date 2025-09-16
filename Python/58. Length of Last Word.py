class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        return len(words[-1])


if __name__ == '__main__':
    obj = Solution()
    print(obj.lengthOfLastWord("luffy is still joyboy"))
