import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # left_sum_list, right_sum_list, left_pointer, right_pointer = [0], [0], 0, len(nums) - 1
        # left_sum, right_sum = 0, 0
        # try:
        #     while left_pointer < len(nums):
        #         left_sum += nums[left_pointer]
        #         left_sum_list.append(left_sum)
        #         right_sum += nums[right_pointer]
        #         right_sum_list.append(right_sum)
        #
        #         left_pointer += 1
        #         right_pointer -= 1
        #
        #     logger.info(f'nums: {nums}')
        #     logger.info(f'left_sum_list: {left_sum_list}')
        #     logger.info(f'right_sum_list: {right_sum_list}')
        #
        #     for i in range(len(nums)):
        #         if left_sum_list[i] == right_sum_list[len(nums)-i-1]:
        #             return i
        #     return -1
        # except Exception as e:
        #     logger.exception(f'exception: {e}')

        total, left_sum = sum(nums), 0
        try:
            for i in range(len(nums)):
                right_sum = total - (nums[i] + left_sum)

                if left_sum == right_sum:
                    return i
                left_sum += nums[i]

            return -1
        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.pivotIndex([1,7,3,6,5,6]))

