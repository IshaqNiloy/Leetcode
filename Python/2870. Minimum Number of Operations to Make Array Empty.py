from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        min_num_of_ops = 0
        nums_occurrence_dict = dict()

        for num in nums:
            if num not in nums_occurrence_dict.keys():
                nums_occurrence_dict[num] = 1
            else:
                nums_occurrence_dict[num] += 1

        for val in nums_occurrence_dict.values():
            if val % 2 != 0 and val % 3 != 0:
                # for prime numbers excluding 1
                if val % 3 == 2 and val != 1:
                    min_num_of_ops += ((val - 2) / 3) + 1
                    continue
                if val % 3 == 1 and val != 1:
                    min_num_of_ops += ((val - 4) / 3) + 2
                    continue
                # ------------end----------------
                # returns -1 if making an empty array is impossible
                return -1
            if val % 3 == 0:
                min_num_of_ops += val / 3
                continue
            if val % 2 == 0:
                # if the number is divisible by 2 and
                # the number can be partitioned into two parts to find the minimum number of operations
                if val % 3 == 2:
                    # if the output of the mod operation is 2 then it follows the following rule
                    # (adding 1 for the second part)
                    min_num_of_ops += ((val - 2) / 3) + 1
                    continue
                if val % 3 == 1:
                    # if the output of the mod operation is 1 then it follows the following rule
                    # (adding 2 for the second part)
                    min_num_of_ops += ((val - 4) / 3) + 2
                    continue
                # ------------end-----------------
                min_num_of_ops += val / 2

        return int(min_num_of_ops)


if __name__ == '__main__':
    obj = Solution()
    result = obj.minOperations([13,7,13,7,13,7,13,13,7])

    print(result)
