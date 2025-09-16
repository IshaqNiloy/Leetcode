import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_string, check_string = '', ''
        str1_dict, str2_dict, gcd_dict = {}, {}, {}

        # construct dict from str1
        for char in str1:
            if char not in str1_dict.keys():
                str1_dict[char] = 1
            else:
                str1_dict[char] += 1

        # construct dict from str2
        for char in str2:
            if char not in str2_dict.keys():
                str2_dict[char] = 1
            else:
                str2_dict[char] += 1

        # construct gcd dict
        if not str1_dict.keys() == str2_dict.keys():
            return ''

        for key in str1_dict.keys():
            gcd_of_two_characters = math.gcd(str1_dict[key], str2_dict[key])
            gcd_dict[key] = gcd_of_two_characters

        # construct gcd string
        for char in str1:
            if gcd_dict[char] > 0:
                gcd_string += char
                gcd_dict[char] -= 1

        # check whether the given strings can be constructed by the gcd_string
        for i in range(int(len(str1)/len(gcd_string))):
            check_string += gcd_string

        if check_string != str1:
            return ''

        check_string = ''
        for i in range(int(len(str2) / len(gcd_string))):
            check_string += gcd_string

        if check_string != str2:
            return ''

        return gcd_string


if __name__ == '__main__':
    obj = Solution()
    result = obj.gcdOfStrings("ABCABC", "ABC")
    print(result)

