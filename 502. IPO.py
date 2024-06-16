import logging

from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_profit_mapping, maximized_capital = dict(), 0
        try:
            for i in range(len(profits)):
                if capital[i] not in capital_profit_mapping:
                    capital_profit_mapping[capital[i]] = [profits[i]]
                else:
                    capital_profit_mapping[capital[i]].append(profits[i])

            logger.info(f'capital profit mapping: {capital_profit_mapping}')

            for _ in range(k):
                if w in capital_profit_mapping:
                    w = max(capital_profit_mapping[w])
                    maximized_capital += w

            return maximized_capital

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    s = Solution()
    logger.info(s.findMaximizedCapital(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]))
