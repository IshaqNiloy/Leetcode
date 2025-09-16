from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_dict = dict()
        group_list = list()
        sub_list = list()
        counter = 1

        for person_id, group_size in enumerate(groupSizes):
            if group_size not in group_dict.keys():
                group_dict[group_size] = [person_id]
            else:
                group_dict[group_size].append(person_id)

        for group_size, id_list in group_dict.items():
            for id in id_list:
                sub_list.append(id)
                if counter == group_size:
                    group_list.append(sub_list)
                    counter = 0
                    sub_list = list()

                counter += 1

        return group_list


if __name__ == '__main__':
    obj = Solution()
    result = obj.groupThePeople([2, 1, 3, 3, 3, 2])
    print(result)


