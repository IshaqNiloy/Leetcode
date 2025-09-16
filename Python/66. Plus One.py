from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_in_string = ''
        final_digit_list = []

        for digit in digits:
            digits_in_string += str(digit)

        for char in str(int(digits_in_string) + 1):
            final_digit_list.append(int(char))

        return final_digit_list

if __name__ == '__main__':
    obj = Solution()
    print(obj.plusOne([9]))