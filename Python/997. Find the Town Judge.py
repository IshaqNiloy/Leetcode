from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        index_judge = 0
        assumed_judge = trust[index_judge][1]
        index = 0

        while True:
            if trust[index][0] != assumed_judge:
                index += 1
                if index == len(trust):
                    return assumed_judge
            else:
                index_judge += 1
                if index_judge == len(trust):
                    return -1
                index = 0
                assumed_judge = trust[index_judge][1]


if __name__ == '__main__':
    obj = Solution()
    result = obj.findJudge(2, [[1,3],[2,3],[3,1]])

    print(result)
