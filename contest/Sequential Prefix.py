from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        prefix_sum = 0
        is_multiple_sub_sequence = False

        if len(nums) == 1:
            return nums[0] + 1

        for index, num in enumerate(nums):
            if index < len(nums) - 1 and num + 1 == nums[index+1]:
                prefix_sum += num
                continue

            if index < len(nums) - 1 and num + 1 != nums[index + 1]:
                dp[index] = prefix_sum + nums[index]
                is_multiple_sub_sequence = True
                prefix_sum = 0

        if not is_multiple_sub_sequence:
            return prefix_sum + nums[len(nums)-1]

        max_prefix_sum = max(dp)
        print(dp)
        if max_prefix_sum not in nums:
            return max_prefix_sum

        while True:
            max_prefix_sum += 1
            if max_prefix_sum not in nums:
                return max_prefix_sum


if __name__ == '__main__':
    obj = Solution()
    result = obj.missingInteger([37])

    print(result)
