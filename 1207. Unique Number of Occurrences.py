from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique_occurrence_dict = dict()

        for item in arr:
            if item not in unique_occurrence_dict.keys():
                unique_occurrence_dict[item] = 1
            else:
                unique_occurrence_dict[item] += 1

        if len(set(unique_occurrence_dict.values())) == len(unique_occurrence_dict.values()):
            return True

        return False


if __name__ == '__main__':
    obj = Solution()
    print(obj.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))


