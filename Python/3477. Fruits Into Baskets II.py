from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        try:
            result = 0
            used_places = []

            for fruit in fruits:
                is_placed = False
                for i in range(len(baskets)):
                    if fruit <= baskets[i] and i not in used_places:
                        used_places.append(i)
                        is_placed = True
                        break
                if not is_placed:
                    result += 1

            return result

        except Exception as e:
            print(e)


if __name__ == "__main__":
    fruits, baskets = [3, 6, 1], [6, 4, 7]
    obj = Solution()
    print(obj.numOfUnplacedFruits(fruits, baskets))
