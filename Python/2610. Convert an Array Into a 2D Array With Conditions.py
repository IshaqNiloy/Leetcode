from typing import List


class Solution:
    @staticmethod
    def findMatrix(nums: List[int]) -> List[List[int]]:
        two_d_arr = []
        sub_arr = []
        minus_one_counter = 0
        end_of_for_loop = False

        while not end_of_for_loop:
            for index, item in enumerate(nums):
                if item != -1 and item not in sub_arr:
                    sub_arr.append(item)
                    nums[index] = -1
                    minus_one_counter += 1
                if index == len(nums) - 1:
                    two_d_arr.append(sub_arr)
                    sub_arr = []
                if minus_one_counter == len(nums):
                    end_of_for_loop = True

        return two_d_arr


if __name__ == '__main__':
    obj = Solution()
    result = obj.findMatrix([1, 2, 3, 4])
    print(result)

