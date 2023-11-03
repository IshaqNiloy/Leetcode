class Solution:
    def reverseWords(self, s: str) -> str:
        stack, sub_string, reversed_string = [], '', ''

        # put the sub_strings into the stack in reverse order
        for char in s:
            if char != ' ':
                sub_string += char
            else:
                stack.append(sub_string)
                sub_string = ''

        stack.append(sub_string)

        # pop the sub_strings from the stack and add them to the reversed_string
        for i in range(len(stack)-1, -1, -1):
            if len(stack[i]) == 0:
                continue
            reversed_string += stack[i] + ' '

        return reversed_string.strip()


if __name__ == '__main__':
    obj = Solution()
    result = obj.reverseWords("a good    example")
    print(result)

