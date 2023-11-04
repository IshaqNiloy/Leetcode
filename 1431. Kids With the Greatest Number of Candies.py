
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        boolean_list = [True] * len(candies)

        for i in range(len(candies)):
            new_count_of_candies = candies[i] + extraCandies
            for candy in candies:
                if new_count_of_candies >= candy:
                    continue
                else:
                    boolean_list[i] = False
                    break

        return boolean_list


if __name__ == '__main__':
    obj = Solution()
    result = obj.kidsWithCandies([12, 1, 12], 10)
    print(result)

