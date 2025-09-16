from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        dp = [0] * len(nums)
        dp[k-1] = sum(nums[0:k])
        max_sum = -1000000000000000000

        if len(nums) == k:
            return sum(nums) / k

        for i in range(k, len(nums)):
            dp[i] = dp[i-1] + nums[i] - nums[i-k]

            if dp[i-1] > max_sum:
                max_sum = dp[i-1]

            if i == len(nums) - 1 and dp[i] > max_sum:
                max_sum = dp[i]

        return max_sum / k


if __name__ == '__main__':
    obj = Solution()
    result = obj.findMaxAverage([0,1,1,3,3], 4)

    print(result)


