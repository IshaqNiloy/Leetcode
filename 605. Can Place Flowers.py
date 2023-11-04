
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        is_flower_place_possible = True
        #
        # if n == 0:
        #     return True
        # if n == 1 and len(flowerbed) == 1 and flowerbed[0] == 1:
        #     return False
        # if n == 1 and len(flowerbed) == 1 and flowerbed[0] == 0:
        #     return True
        #
        # for i in range(len(flowerbed)):
        #     # if the pattern is 0, 0, 1 at the very beginning of the iteration
        #     if i == 0 and flowerbed[i] == flowerbed[i+1] == 0 and flowerbed[i+2] == 1:
        #         flowerbed[i] = 1
        #         n -= 1
        #         if n == 0:
        #             break
        #
        #     # if the pattern is 0, 0, 0 and it is the general case
        #     elif i < len(flowerbed) - 2 and flowerbed[i] == flowerbed[i+1] == flowerbed[i+2] == 0:
        #         flowerbed[i+1] = 1
        #         n -= 1
        #         if n == 0:
        #             break
        #
        #     # if the pattern is 1, 0, 0 at the very end of the iteration
        #     elif i == len(flowerbed) - 3 and flowerbed[i] == 1 and flowerbed[i + 1] == flowerbed[i + 2] == 0:
        #         flowerbed[i] = 1
        #         n -= 1
        #         if n == 0:
        #             break
        #
        # if n != 0:
        #     is_flower_place_possible = False

        for i in range(1, len(flowerbed)):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    break

        for i in range(len(flowerbed)-2, -1, -1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    break

        return is_flower_place_possible


if __name__ == '__main__':
    obj = Solution()
    result = obj.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2)
    print(result)

