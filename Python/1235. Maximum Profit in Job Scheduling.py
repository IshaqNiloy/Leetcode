import bisect
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [[0, 0]]  # [time, profit]

        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1  # Find the latest job that ends before the current job starts
            if dp[i][1] + p > dp[-1][1]:  # Check if adding the current job is more profitable
                dp.append([e, dp[i][1] + p])  # Update the maximum profit at this time
        return dp[-1][1]


if __name__ == '__main__':
    obj = Solution()
    result = obj.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70])

    print(result)

