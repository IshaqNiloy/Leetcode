from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        answer_dict = dict()
        answer_list = list()

        for i in range(len(nums)):
            if nums[i] not in answer_dict.keys():
                answer_dict[nums[i]] = 1
                continue
            else:
                # adds duplicate number
                answer_list.append(nums[i])
                break

        for i in range(1, len(nums) + 1):
            # adds missing number
            if i not in nums:
                answer_list.append(i)
                break

        return answer_list


if __name__ == '__main__':
    obj = Solution()
    result = obj.findErrorNums([2,2])

    print(result)

