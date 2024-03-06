class Solution:
    def minimumLength(self, s: str) -> int:
        length_of_s = len(s)
        start_pointer, end_pointer = 0, length_of_s - 1

        if s[start_pointer] != s[end_pointer]:
            return length_of_s

        while start_pointer < end_pointer:
            if s[start_pointer] == s[end_pointer]:
                start_pointer += 1
                end_pointer -= 1
            else:
                if s[end_pointer-1] == s[end_pointer]:
                    end_pointer -= 1
                elif start_pointer == 0:
                    start_pointer += 1
                elif s[start_pointer] == s[start_pointer-1]:
                    start_pointer += 1

        return len(s[start_pointer:end_pointer+1])


if __name__ == '__main__':
    obj = Solution()
    result = obj.minimumLength('aabccabba')

    print(result)

