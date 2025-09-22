from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        try:
            # The items of the numbers list are sorted in non-decreasing order
            # Two pointers approach
            first_pointer = 0
            second_pointer = len(numbers) - 1

            while numbers[first_pointer] + numbers[second_pointer] != target:
                sum = numbers[first_pointer] + numbers[second_pointer]
                # If the sum is greater than target then it is quite obvious that 
                # we have to move to the left to make sum closer to the target.
                if sum > target:
                    second_pointer -= 1
                # If the sum is less than target then it is quite obvious that 
                # we have to move to the right to make sum closer to the target.
                elif sum < target:
                    first_pointer += 1

            return [first_pointer + 1, second_pointer + 1]

        except Exception as e:
            print(e) 


if __name__ == '__main__':
    obj = Solution()
    print(obj.twoSum([1,2,3,4], 3))