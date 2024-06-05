from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        starting_window_size, max_window_size, subarray_counter = 1 if goal == 0 else goal, len(nums), 0

        for window_size in range(starting_window_size, max_window_size+1):
            i = subarray_sum = 0

            while i+window_size <= len(nums):
                if i != 0:
                    subarray_sum = (subarray_sum - nums[i - 1]) + nums[i + window_size - 1]
                else:
                    subarray_sum = sum(nums[0:window_size])

                if subarray_sum == goal:
                    subarray_counter += 1

                i += 1

        return subarray_counter


if __name__ == '__main__':
    obj = Solution()
    result = obj.numSubarraysWithSum([1,0,1,0,1], 2)
    print(result)
