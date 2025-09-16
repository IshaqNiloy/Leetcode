from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_first_n_numbers = int(n*(n+1)/2)

        sum_of_elements_of_list = sum(nums)

        return sum_of_first_n_numbers - sum_of_elements_of_list


if __name__ == '__main__':
    obj = Solution()
    result = obj.missingNumber([9,6,4,2,3,5,7,0,1])

    print(result)

