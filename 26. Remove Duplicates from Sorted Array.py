from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = set(nums)
        nums.clear()
        for item in new_list:
            nums.append(item)
        print(nums)
        return len(nums)


if __name__ == '__main__':
    obj = Solution()
    print(obj.removeDuplicates([1,1,2]))