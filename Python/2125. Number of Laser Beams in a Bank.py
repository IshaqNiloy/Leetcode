from typing import List


class Solution:
    @staticmethod
    def numberOfBeams(bank: List[str]) -> int:
        total_num_of_beams = 0

        for index, outer_row in enumerate(bank):
            if '1' in outer_row:
                first_row_num_of_devices = outer_row.count('1')
                for inner_row in bank[index+1:]:
                    if '1' in inner_row:
                        second_row_num_of_devices = inner_row.count('1')
                        total_num_of_beams += first_row_num_of_devices * second_row_num_of_devices
                        break

        return total_num_of_beams


if __name__ == '__main__':
    obj = Solution()
    result = obj.numberOfBeams(["000", "111", "000"])

    print(result)
