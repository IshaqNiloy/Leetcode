from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str])->List[List[str]]:
        try:
            result = list() 
            wordGroupMapping = dict()

            for word in strs:
                sortedWord = ''.join(sorted(word))
                if sortedWord in wordGroupMapping:
                    wordGroupMapping[sortedWord].append(word)
                else:
                    wordGroupMapping[sortedWord] = [word]

            for key in wordGroupMapping:
                result.append(wordGroupMapping[key])

            return result
        except Exception as e:
            print(e)
        

if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))