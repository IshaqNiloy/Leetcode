from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        try:
            newNums = nums
            tempNums = list()
            windowSize = 2

            while len(newNums) > 1:
              tempNums = newNums
              newNums = list()
              for i in range(0, len(tempNums) - 1):
                  newNums.append((tempNums[i] + tempNums[i+1]) % 10)
              tempNums = list()

            return newNums[0]      
        except Exception as e:
            print(e)

if __name__ == '__main__':
    obj = Solution()
    print(obj.triangularSum([5]))