from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # instead of trying to move the zeros to the right we will try to move the non-zero values to the left
        # use two pointers like left and right pointer
        for left_pointer in range(len(nums)):
            if nums[left_pointer] == 0:
                for right_pointer in range(left_pointer+1, len(nums)):
                    if nums[right_pointer] != 0:
                        nums[left_pointer] = nums[right_pointer]
                        nums[right_pointer] = 0
                        break


if __name__ == '__main__':
    obj = Solution()
    obj.moveZeroes([0,1,0,3,12])
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        # wait while we find a non-zero element to
        # swap with you
        if nums[slow] != 0:
            slow += 1

