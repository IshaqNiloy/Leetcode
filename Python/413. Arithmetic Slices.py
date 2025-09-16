from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # sliding window and dp concept has been used here
        dp = [0] * len(nums)

        if len(nums) < 3:
            return 0

        for i in range(len(nums)):
            if i < len(nums) - 2 and nums[i] - nums[i+1] == nums[i+1] - nums[i+2]:
                dp[i] = 1 + dp[i-1]

        return sum(dp)


if __name__ == '__main__':
    obj = Solution()
    result = obj.numberOfArithmeticSlices([7])

    print(result)
