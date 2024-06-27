import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        try:
            edge1 = edges[0]
            edge2 = edges[1]

            if edge1[0] == edge2[0] or edge1[0] == edge2[1]:
                return edge1[0]
            return edge1[1]

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.findCenter(edges = [[1,2],[2,3],[4,2]]))
