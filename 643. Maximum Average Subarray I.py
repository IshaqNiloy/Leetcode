from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        for i in range(len(nums)):
            if i < i + k:
                total = sum(nums[i:i+k])


if __name__ == '__main__':
    obj = Solution()
    result = obj.findMaxAverage([1,12,-5,-6,50,3], 4)

    print(result)