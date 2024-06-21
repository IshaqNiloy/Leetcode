import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def is_possible(self, positions_sorted: List[int], mid: int, number_of_balls: int) -> bool:
        last_position = positions_sorted[0]
        counter = 1

        for i in range(len(positions_sorted)):
            if positions_sorted[i] - last_position >= mid:
                counter += 1
                last_position = positions_sorted[i]
                if counter == number_of_balls:
                    return True

        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        positions_sorted = sorted(position)
        min_position, max_position, left, right, ans = (positions_sorted[0], positions_sorted[-1],
                                                        1, positions_sorted[-1] - positions_sorted[0], 0)

        try:
            if m == 2:
                return max_position - min_position

            while left <= right:
                mid = (left + right) // 2
                logger.info(f'mid value: {mid}')

                if self.is_possible(positions_sorted=positions_sorted, mid=mid, number_of_balls=m):
                    left = mid + 1
                    ans = max(ans, mid)
                else:
                    right = mid - 1

            return ans

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.maxDistance(position = [1,2,3,4,5,6,7,8,9,10], m = 4))
