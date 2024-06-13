import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats_sorted, students_sorted, min_moves = sorted(seats), sorted(students), 0
        try:
            for i in range(len(seats)):
                min_moves += abs(seats_sorted[i] - students_sorted[i])

            return min_moves

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.minMovesToSeat([3,1,5], [2,7,4]))