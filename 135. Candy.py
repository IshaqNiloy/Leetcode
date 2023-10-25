from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        list_size = len(ratings)
        list_of_candy = [1] * list_size
        min_num_of_candies = len(ratings)
        for curr in range(len(ratings)):
            previous = curr - 1
            next = curr + 1
            print(list_of_candy)
            # case -> general case
            if previous >= 0 and next < len(ratings):
                if ratings[curr] > ratings[previous] or ratings[curr] > ratings[next]:
                    if ratings[curr] > ratings[previous]:
                        min_num_of_candies += list_of_candy[previous]
                        list_of_candy[curr] = list_of_candy[previous] + 1
                    else:
                        min_num_of_candies += 1
                        list_of_candy[curr] += 1
            # case -> 2 when the current index is at the beginning of the list
            elif previous < 0:
                if ratings[curr] > ratings[next]:
                    min_num_of_candies += 1
                    list_of_candy[curr] += 1

            # case -> 3 when the current index is at the end of the list
            elif next == len(ratings):
                if ratings[curr] > ratings[previous]:
                    min_num_of_candies += list_of_candy[previous]
                    list_of_candy[curr] = list_of_candy[previous] + 1

        return min_num_of_candies


if __name__ == '__main__':
    obj = Solution()
    result = obj.candy([1,2,87,87,87,2,1])
    print(result)
    # Input: ratings = [1, 0, 2]
    # Output: 5
    # Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

