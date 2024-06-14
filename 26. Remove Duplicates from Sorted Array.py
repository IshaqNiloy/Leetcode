from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums_list = list(set(nums))
        nums.clear()
        for item in sorted(unique_nums_list):
            nums.append(item)

        return len(nums)


if __name__ == '__main__':
    obj = Solution()
    print(obj.removeDuplicates([-1,0,0,0,0,3,3]))