from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # To get a hill or valley there should be at least 3 elements in the list.
        if len(nums) == 1 or len(nums) == 2:
            return 0

        hill_valley_count, left_element, right_element = 0, 0, 0
        # Avoid first and last element of the list since they can not be a hill or valley.
        for i in range(1, len(nums) - 1):
            current_element = nums[i]
            previous_element = nums[i - 1]
            # If current_element and previous element are same then it means that
            # they are part of the same hill or valley.
            if current_element == previous_element:
                continue
            # Go to left side of the list
            left_index = i - 1
            while left_index > -1:
                if nums[left_index] != current_element:
                    left_element = nums[left_index]
                    break
                left_index -= 1

            # Go to right side of the list
            right_index = i + 1
            while right_index < len(nums):
                if nums[right_index] != current_element:
                    right_element = nums[right_index]
                    break
                right_index += 1
            # If the current_element is greater than its left and right element then it is a hill.
            # If the current_element is smaller than its left and right element then it is a valley.
            if (left_element != 0 and right_element != 0) and (
                    left_element < current_element > right_element or left_element > current_element < right_element):
                hill_valley_count += 1

        return hill_valley_count


if __name__ == '__main__':
    nums = [38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38,
            38, 38, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98]
    obj = Solution()
    print(obj.countHillValley(nums))
