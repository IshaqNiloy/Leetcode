class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for char in s:
            if char not in dict_s.keys():
                dict_s[char] = 1
            else:
                dict_s[char] += 1

        for char in t:
            if char not in dict_t.keys():
                dict_t[char] = 1
            else:
                dict_t[char] += 1

        if dict_s == dict_t:
            return True
        return False


if __name__ == '__main__':
    obj = Solution()
    print(obj.isAnagram('cat', 'rat'))

