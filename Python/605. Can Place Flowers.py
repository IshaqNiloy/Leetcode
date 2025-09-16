
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # if there is no flower to put we consider it as True
        if n == 0:
            return True

        is_flower_place_possible = True

        # all the cases can be covered or put in the general case by just adding 0 at the beginning and end of the list
        flowerbed.insert(0, 0)
        flowerbed.append(0)

        for i in range(len(flowerbed)):
            # if the pattern is 0, 0, 0 and it is the general case
            if i < len(flowerbed) - 2 and flowerbed[i] == flowerbed[i+1] == flowerbed[i+2] == 0:
                flowerbed[i+1] = 1
                n -= 1
                if n == 0:
                    break

        if n != 0:
            is_flower_place_possible = False

        return is_flower_place_possible


if __name__ == '__main__':
    obj = Solution()
    result = obj.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2)
    print(result)

