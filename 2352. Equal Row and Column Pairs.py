import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_map, col_map, equal_pair_counter, full_col = dict(), dict(), 0, list()
        try:
            for row in grid:
                if tuple(row) not in row_map:
                    row_map[tuple(row)] = 1
                else:
                    row_map[tuple(row)] += 1

            logger.info(f'row column map: {row_map}')
            row, col = 0, 0

            while col < len(grid[0]):
                while row < len(grid):
                    full_col.append(grid[row][col])

                    if row == len(grid) - 1:
                        if tuple(full_col) not in col_map:
                            col_map[tuple(full_col)] = 1
                        else:
                            col_map[tuple(full_col)] += 1

                    row += 1

                full_col, row = list(), 0
                col += 1

            logger.info(f'column map: {col_map}')

            for key in row_map:
                if key in col_map:
                    equal_pair_counter += row_map[key] * col_map[key]

            return equal_pair_counter

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
