from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        common_subsequence = ''
        starting_index = 0
        big_text, small_text = (text1, text2) if len(text1) > len(text2) else (text2, text1)

        for i in small_text:
            for j in range(starting_index, len(big_text)):
                if i == big_text[j]:
                    common_subsequence += i
                    starting_index = j + 1
                    break

        print(common_subsequence)
        return len(common_subsequence)


if __name__ == '__main__':
    obj = Solution()
    result = obj.longestCommonSubsequence('oxcpqrsvwf', 'shmtulqrypy')

    print(result)

