from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_occurrence_mapping = dict()

        for num in nums:
            if num not in num_occurrence_mapping.keys():
                num_occurrence_mapping[num] = 1
            else:
                num_occurrence_mapping[num] += 1

        return max(num_occurrence_mapping, key=lambda k: num_occurrence_mapping[k])


if __name__ == '__main__':
    obj = Solution()
    result = obj.majorityElement([2, 2, 1, 1, 1, 2, 2])

    print(result)

