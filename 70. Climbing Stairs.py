import time
from datetime import timezone, datetime


class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        # Base cases
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        # Check if the result for 'n' is already in the memo dictionary
        if n in memo:
            return memo[n]

        # Recursive case: distinct ways for n steps is the sum of distinct ways for (n-1) and (n-2) steps
        ways = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)

        # Cache the result in the memo dictionary
        memo[n] = ways

        return ways


if __name__ == '__main__':
    obj = Solution()
    start_time = time.time()
    result = obj.climbStairs(100)
    end_time = time.time()
    print(f'programme execution time: {(end_time - start_time)*1000} ms')

    print(result)
