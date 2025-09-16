import logging

from typing import List
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num_frequency_mapping, result, sorted_nums = dict(), list(), list()
        try:
            for item in arr1:
                if item not in num_frequency_mapping:
                    num_frequency_mapping[item] = [item]
                else:
                    num_frequency_mapping[item].append(item)

                if item not in arr2:
                    sorted_nums.append(item)

            logger.info(f'number frequency mapping: {num_frequency_mapping}')

            for num in arr2:
                result += num_frequency_mapping[num]

            sorted_nums.sort()

            logger.info(f'sorted list: {sorted_nums}')

            return result + sorted_nums
        except Exception as e:
            logger.info(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(f'result: {s.relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6])}')