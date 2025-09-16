from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pref_length, counter = len(pref), 0
        for word in words:
            if word[:pref_length] == pref:
                counter += 1
        return counter


if __name__ == '__main__':
    words =  ["leetcode","win","loops","success"]
    pref = "code"
    obj = Solution()
    print(obj.prefixCount(words, pref))