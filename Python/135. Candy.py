from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        list_size = len(ratings)
        # since every child must get at least one candy
        list_of_candy = [1] * list_size

        # going from left to right and always comparing with the child who is behind the current child
        for curr in range(1, list_size):
            if ratings[curr] > ratings[curr-1]:
                # no need to add one since the every child already has one
                list_of_candy[curr] += list_of_candy[curr-1]

        # going from right to left and always comparing with the child who is behind the current child
        for curr in range(list_size-2, -1, -1):
            # rating is higher but the number of candy is equal or lower
            if ratings[curr] > ratings[curr+1]:
                if list_of_candy[curr] <= list_of_candy[curr+1]:
                    list_of_candy[curr] += list_of_candy[curr+1] - list_of_candy[curr] + 1

        return sum(list_of_candy)


if __name__ == '__main__':
    obj = Solution()
    result = obj.candy([1,6,10,8,7,3,2])
    print(result)
    # Input: ratings = [1, 0, 2]
    # Output: 5
    # Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

