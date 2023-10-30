from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence_length = 0
        sequence_length = 0

        for num in nums:
            # checking if we can consider it as the beginning of a sequence. If it is the start of a sequence then it
            if (num - 1) not in nums:
                while num in nums:
                    sequence_length += 1
                    num += 1

            longest_sequence_length = max(longest_sequence_length, sequence_length)
            sequence_length = 0

        return longest_sequence_length


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestConsecutive([100,4,200,1,3,2]))

