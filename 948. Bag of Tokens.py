from typing import List, Optional
from main import ListNode


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        sorted_tokens = sorted(tokens)
        start_pointer = 0
        end_pointer = len(sorted_tokens) - 1
        score = 0

        while start_pointer <= end_pointer:
            if sorted_tokens[start_pointer] <= power:
                power -= sorted_tokens[start_pointer]
                score += 1
                start_pointer += 1

            elif 1 <= score and start_pointer != end_pointer:
                power += sorted_tokens[end_pointer]
                score -= 1
                end_pointer -= 1

            else:
                start_pointer += 1

        return score


if __name__ == '__main__':
    obj = Solution()
    result = obj.bagOfTokensScore([55,71,82], 54)

    print(result)
