import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def __init__(self):
        super().__init__()
        self.grid = None
        self.ROW = None
        self.COL = None
        self.visited_island = None

    def dfs(self, row: int, col: int) -> int:
        if (row < 0 or row == self.ROW or col < 0 or col == self.COL or self.grid[row][col] == '0'
                or (row, col) in self.visited_island):
            return 0

        self.visited_island.add((row, col))

        self.dfs(row + 1, col) + self.dfs(row - 1, col) + self.dfs(row, col + 1) + self.dfs(row, col - 1)

        return 1

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid, self.ROW, self.COL, self.visited_island, number_of_islands = grid, len(grid), len(grid[0]), set(), 0

        try:
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    number_of_islands += self.dfs(row=row, col=col)
            return number_of_islands
        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.numIslands([["1","1","0","0","0"],
                              ["1","1","0","0","0"],
                              ["0","0","1","0","0"],
                              ["0","0","0","1","1"]]))
