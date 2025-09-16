from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        try:
            sorted_with_index = sorted(enumerate(baskets), key=lambda k: k[1])
            print(sorted_with_index)
            return 0

        except Exception as e:
            print(e)


if __name__ == "__main__":
    fruits, baskets = [3, 6, 1], [6, 4, 7]
    obj = Solution()
    print(obj.numOfUnplacedFruits(fruits, baskets))
