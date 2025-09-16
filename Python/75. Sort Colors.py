from typing import List
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        num_frequency_mapping, sorted_colors = dict(), [0, 1, 2]

        try:
            for num in nums:
                if num not in num_frequency_mapping:
                    num_frequency_mapping[num] = [num]
                else:
                    num_frequency_mapping[num].append(num)

            logger.info(f'num frequency mapping: {num_frequency_mapping}')

            nums.clear()
            for color in sorted_colors:
                if color in num_frequency_mapping.keys():
                    nums += num_frequency_mapping[color]

            logger.info(f'sorted colors: {nums}')

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    nums_list = [1]
    s.sortColors(nums = nums_list)
    logger.info(f'result: {nums_list}')