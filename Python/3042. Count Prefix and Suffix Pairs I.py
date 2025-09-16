from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        try:
            counter = 0
            for i in range(len(words)):
                for j in range(i+1, len(words)):
                    if words[i] == words[j][:len(words[i])] and words[i] == words[j][len(words[j])-len(words[i]):]:
                        counter +=1
            return counter
        except Exception as e:
            print('Error: ', e)

if __name__ == '__main__':
    words = ["a","aba","ababa","aa"]
    obj = Solution()
    print(obj.countPrefixSuffixPairs(words))