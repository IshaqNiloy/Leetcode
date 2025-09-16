from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix, answer = [1], [1], []
        postfix_counter = 0

        # find prefix
        for i in range(len(nums)):
            prefix.append(prefix[i] * nums[i])

        # find postfix
        for i in range(len(nums)-1, -1, -1):
            postfix.append(postfix[postfix_counter] * nums[i])
            postfix_counter += 1

        postfix.reverse()

        for i in range(len(prefix) - 1):
            answer.append(prefix[i] * postfix[i+1])

        return answer


if __name__ == '__main__':
    obj = Solution()
    print(obj.productExceptSelf([-1, 1, 0, -3, 3]))
