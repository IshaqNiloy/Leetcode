from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        try:
            result = []
            for word in words1:
                words2_copy = list(set(char for item in words2.copy() for char in item))
                for letter in word:
                    if letter in words2_copy:
                        words2_copy.remove(letter)
                if len(words2_copy) == 0:
                    result.append(word)
            return result
        except Exception as e:
            print('Error: ', e)

if __name__ == '__main__':
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["e", "oo"]
    obj = Solution()
    print(obj.wordSubsets(words1, words2))