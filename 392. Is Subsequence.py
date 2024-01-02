class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if s is an empty string then return True
        if len(s) == 0:
            return True

        i = 0
        for char in t:
            # make sure the index is not out of range
            if i <= len(s) - 1 and s[i] == char:
                i += 1

        # if s is a subsequence of t then i and the length of s will be equal
        if len(s) == i:
            return True

        return False


if __name__ == '__main__':
    s = 'a'
    t = 'ahbgdc'

    obj = Solution()
    result = obj.isSubsequence(s, t)

    print(result)
