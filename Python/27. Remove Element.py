from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        try:
            number_of_replacements = 0
            for i in range(len(nums)):
                if nums[i] == val:
                    nums[i] = 100
                    number_of_replacements += 1
            nums.sort()
            return len(nums) - number_of_replacements
        except Exception as err:
            print(err)


if __name__ == '__main__':
    obj = Solution()
    nums = [0,1,2,2,3,0,4,2]
    print(obj.removeElement(nums, 2))
    print(nums)