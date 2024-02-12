class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        counter = 0
        vowels = 'aeiou'
        for i in range(len(s)):
            for char in s[i:i+k]:
                if char in vowels:
                    counter += 1


if __name__ == '__main__':
    obj = Solution()
    result = obj.maxVowels("abciiidef", 3)

    print(result)