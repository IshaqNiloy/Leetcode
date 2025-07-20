from typing import List

from sqlparse.utils import consume


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                if nums[i] > target:
                    return i
            return len(nums)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    obj = Solution()
    print(obj.searchInsert([1,3,5,6], 2))