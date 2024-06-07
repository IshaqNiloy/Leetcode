# Please write a function that searches in an array of a numeric values for the value
# that is closest to a given value N. If there are two values that are equally far away,
# return the greater value.
#
# searchClosest(4.5, array(6, 0, -1.5, 4.4, 7, 5));
# => 4.4
#
# searchClosest(5.5, array(6, 0, -1.5, 4.4, 7, 5));
# => 6
import math


def searchClosest(a: int, arr: list) -> int:
    minimum_value, result = 9999999, 0

    try:
        for item in arr:
            curr_minimum_value = math.fabs(a - item)
            if curr_minimum_value < minimum_value:
                minimum_value = curr_minimum_value
                result = item

        return result
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print(searchClosest(1, [-1, 3]))

