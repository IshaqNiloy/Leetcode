import logging
import math

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_frequency_mapping, pairs, max_k_sum_pairs = dict(), 0, 0
        try:
            for num in nums:
                if num not in num_frequency_mapping:
                    num_frequency_mapping[num] = 1
                else:
                    num_frequency_mapping[num] += 1

            logger.info(f'number frequency map: {num_frequency_mapping}')

            for first_key in num_frequency_mapping:
                second_key = k - first_key

                if first_key == second_key:
                    max_k_sum_pairs += math.floor(num_frequency_mapping[first_key] / 2)
                    num_frequency_mapping[first_key] = 0

                elif second_key in num_frequency_mapping:
                    max_k_sum_pairs += min(num_frequency_mapping[first_key], num_frequency_mapping[second_key])
                    num_frequency_mapping[first_key] = 0
                    num_frequency_mapping[second_key] = 0

            return max_k_sum_pairs
        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.maxOperations([3,1,3,4,3], 6))
