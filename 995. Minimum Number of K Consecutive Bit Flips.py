import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        counter, nums_sum, prefix_sum, left, right, window_sum = 0, 0, 0, 0, 0, 0
        logger.info(f'initial nums: {nums}')

        try:
            # for index, num in enumerate(nums):
                # nums_sum += num
                # if num == 0 and index + k <= len(nums):
                #     for i in range(index, index + k):
                #         if nums[i] == 0:
                #             nums[i] = 1
                #         else:
                #             nums[i] = 0
                #     counter += 1
                # prefix_sum += nums[index]
            while right < len(nums):
                window_sum += nums[right]

                if right < k and nums[right] == 0:
                    counter = 1
                    prefix_sum += 1

                if k <= right:
                    window_sum -= nums[left]
                    left += 1

                    if nums[right] == 0:
                        counter += 1

                    prefix_sum += 1

                right += 1

            if 0 not in set(nums):
                return 0
            print(counter)
            if prefix_sum == len(nums):
                return counter

            return -1

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.minKBitFlips(nums = [1,1,0], k = 2))
