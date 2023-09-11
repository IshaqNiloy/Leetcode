from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = list(set(nums))

        old_list_len = len(nums)
        new_list_len = len(new_list)

        diff = old_list_len - new_list_len

        for _ in range(diff):
            new_list.append('_')

        print(new_list)
        return new_list_len


if __name__ == '__main__':
    obj = Solution()
    print(obj.removeDuplicates([1, 1, 2, 3]))