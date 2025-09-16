import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs_sorted, worker_sorted, max_profit = sorted(zip(difficulty, profit)), sorted(worker), 0
        logger.info(f'jobs sorted: {jobs_sorted}')

        try:
            for w in worker_sorted:
                for index, job in enumerate(jobs_sorted):
                    if w == job[0]:
                        max_profit += job[1]
                        break
                    elif jobs_sorted[index - 1][0] < w < job[0]:
                        max_profit += jobs_sorted[index - 1][1]
                        break
                    elif index == len(difficulty) - 1 and jobs_sorted[index][0] < w:
                        max_profit += jobs_sorted[index][1]

            return max_profit
        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.maxProfitAssignment(difficulty=[68,35,52,47,86], profit=[67,17,1,81,3], worker=[92,10,85,84,82]))
