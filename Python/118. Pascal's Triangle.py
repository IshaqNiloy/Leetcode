import time
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        sub_list = []
        dict_of_two_sum = {}

        for i in range(1, numRows + 1):
            if i == 1:
                result.append([1])
                continue
            elif i == 2:
                result.append([1, 1])
                continue
            else:
                for j in range(i - 2):
                    index_of_sum_list = i - 2
                    index_of_item_of_sub_list = j

                    sum_from_dict = dict_of_two_sum.get(
                        str(result[index_of_sum_list][index_of_item_of_sub_list]) + ' + ' +
                        str(result[index_of_sum_list][index_of_item_of_sub_list + 1]))
                    if sum_from_dict:
                        sum = sum_from_dict
                    else:
                        sum = (result[index_of_sum_list][index_of_item_of_sub_list] +
                               result[index_of_sum_list][index_of_item_of_sub_list + 1])

                        dict_of_two_sum[str(result[index_of_sum_list][index_of_item_of_sub_list]) + ' + ' +
                                        str(result[index_of_sum_list][index_of_item_of_sub_list + 1])] = sum

                    sub_list.append(sum)

            sub_list.insert(0, 1)
            sub_list.append(1)
            result.append(sub_list)
            sub_list = []

        return result


if __name__ == '__main__':
    start_time = time.time()
    obj = Solution()
    result = obj.generate(50)
    end_time = time.time()
    print(result)
    execution_time = end_time - start_time
    print(execution_time)
