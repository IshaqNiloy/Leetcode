from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = 0
        dp = [{} for _ in nums]

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
                total += dp[j].get(diff, 0)

        return total


if __name__ == '__main__':
    obj = Solution()
    result = obj.numberOfArithmeticSlices([2,4,6,8,10])

    print(result)
