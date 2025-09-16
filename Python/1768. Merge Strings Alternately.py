class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ''
        i = 0

        while True:
            try:
                if i < len(word1):
                    merged_string += word1[i]
                if i < len(word2):
                    merged_string += word2[i]
            except Exception as e:
                print(f'exception: {e}')

            i += 1
            if i > len(word1) and i > len(word2):
                break

        return merged_string


if __name__ == '__main__':
    test = Solution()
    print(test.mergeAlternately('ali', 'ishaq'))
