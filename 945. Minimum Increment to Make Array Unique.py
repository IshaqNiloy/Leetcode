import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # num_frequency_mapping, nums_set, increment_counter, new_num = dict(), set(nums), 0, 0
        increment_counter, sorted_nums, left, right = 0, sorted(nums), 0, 1
        try:
            # brute force approach that exceeds time
            # for num in nums:
            #     if num not in num_frequency_mapping:
            #         num_frequency_mapping[num] = 1
            #     else:
            #         num_frequency_mapping[num] += 1
            #
            # logger.info(f'number frequency mapping: {num_frequency_mapping}')
            #
            # for num in num_frequency_mapping:
            #     if num_frequency_mapping[num] > 1:
            #         new_num = num
            #         while num_frequency_mapping[num] != 1:
            #             logger.info(f'new num: {new_num}')
            #             new_num += 1
            #             increment_counter += 1
            #
            #             logger.info(f'increment counter: {increment_counter}')
            #             if new_num not in nums_set:
            #                 num_frequency_mapping[num] -= 1
            #                 nums_set.add(new_num)
            #                 new_num = num
            #
            # logger.info(f'nums set: {nums_set}')

            # sorting and two pointers approach that passes all the test cases
            for _ in range(len(sorted_nums)):
                if right < len(sorted_nums) and sorted_nums[left] == sorted_nums[right]:
                    sorted_nums[right] += 1
                    increment_counter += 1
                elif right < len(sorted_nums) and sorted_nums[left] > sorted_nums[right]:
                    increment_counter += sorted_nums[left] - sorted_nums[right] + 1
                    sorted_nums[right] += sorted_nums[left] - sorted_nums[right] + 1

                left += 1
                right += 1

            return increment_counter

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.minIncrementForUnique([3,2,1,2,1,7]))
