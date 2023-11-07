from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # convert the lists to sets to make the program more efficient
        nums1_set, nums2_set, answer = set(nums1), set(nums2), [[], []]

        for item in nums1_set:
            if item not in nums2_set:
                answer[0].append(item)

        for item in nums2_set:
            if item not in nums1_set:
                answer[1].append(item)

        return answer


if __name__ == '__main__':
    obj = Solution()
    result = obj.findDifference([1, 2, 3, 3], [1, 1, 2, 2])
    print(result)
