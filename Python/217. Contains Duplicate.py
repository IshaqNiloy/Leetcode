from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return False
        return True


if __name__ == '__main__':
    obj = Solution()
    print(obj.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
