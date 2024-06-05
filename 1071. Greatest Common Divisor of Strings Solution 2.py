import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        common_sub_string = ''

        try:
            # finds the minimum iteration
            if len(str1) < len(str2):
                number_of_iterations = len(str1)
            else:
                number_of_iterations = len(str2)

            # finds longest common sub string
            for i in range(number_of_iterations):
                if str1[i] == str2[i]:
                    common_sub_string += str1[i]

            # if there is no common sub string
            if common_sub_string == '':
                return ''

            # initializes variables
            concatenated_str1 = concatenated_str2 = common_sub_string
            logger.info(f'initial common sub string: {common_sub_string}')

            while True:
                if len(concatenated_str1) < len(str1):
                    concatenated_str1 += common_sub_string
                if len(concatenated_str2) < len(str2):
                    concatenated_str2 += common_sub_string
                if concatenated_str1 == str1 and concatenated_str2 == str2:
                    return common_sub_string
                if ((len(concatenated_str1) >= len(str1) and concatenated_str1 != str1)
                        or len(concatenated_str2) >= len(str2) and concatenated_str2 != str2):
                    if len(common_sub_string) == 1:
                        return ''
                    common_sub_string = common_sub_string[:len(common_sub_string)-1]
                    concatenated_str1 = concatenated_str2 = common_sub_string

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    obj = Solution()
    result = obj.gcdOfStrings("ABABAB", "ABAB")
    print(result)

