class Solution:
    def reverseVowels(self, s: str) -> str:
        stack, list_of_chars_with_reversed_vowels, string_with_reversed_vowels = [], [], ''
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # put all the vowels of the given string in a stack
        for char in s:
            if char in vowels:
                stack.append(char)

        reversed_index = len(stack) - 1

        # replace only the vowels with the vowels that are stored in the stack by poping
        for char in s:
            if char in vowels:
                list_of_chars_with_reversed_vowels += stack[reversed_index]
                reversed_index -= 1
            else:
                list_of_chars_with_reversed_vowels += char

        return string_with_reversed_vowels.join(list_of_chars_with_reversed_vowels)


if __name__ == '__main__':
    obj = Solution()
    result = obj.reverseVowels('leetcode')
    print(result)

