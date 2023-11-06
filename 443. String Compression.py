from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        s, selected_char, counter = '', chars[0], 0

        # keep counting the same character until a new character appears
        for char in chars:
            # keep counting the same character until a new character appears
            if char == selected_char:
                counter += 1
            # update selected_char when a new character appears
            else:
                s += selected_char
                # no need to add the counter if the character appears only once. Just add the character
                if counter != 1:
                    s += str(counter)
                selected_char = char
                counter = 1

        # for the last character and its counter
        s += selected_char
        if counter != 1:
            s += str(counter)

        # clears the original list and adds individual characters of string s to it
        chars.clear()
        for char in s:
            chars.append(char)

        return len(chars)


if __name__ == '__main__':
    obj = Solution()
    result = obj.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
    print(result)
