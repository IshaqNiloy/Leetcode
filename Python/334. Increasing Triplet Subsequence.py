from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # if the length of the list is less than 3 then it is not possible to find a triplet
        if len(nums) < 3:
            return False

        smallest = second_smallest = float('inf')

        # find smallest, second smallest and a number that is greater than both smallest and second smallest
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= second_smallest:
                second_smallest = num
            else:
                return True

        return False


if __name__ == '__main__':
    obj = Solution()
    print(obj.increasingTriplet([2,1,5,0,4,6]))

