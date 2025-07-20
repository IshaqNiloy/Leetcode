class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        if needle == haystack:
            return 0

        start_pointer = 0
        end_pointer = len(needle)

        while end_pointer <= len(haystack):
            if haystack[start_pointer:end_pointer] == needle:
                return start_pointer
            else:
                start_pointer += 1
                end_pointer += 1

        return -1

if __name__ == '__main__':
    obj = Solution()
    print(obj.strStr("abc", "c"))