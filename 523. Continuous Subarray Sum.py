import logging, time

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Solution(object):
    def checkSubarraySum(self, nums: list, k: int) -> bool:
        # The following solution is correct, but it has a time complexity of O(n2) which is not very efficient
        # window_size = 2
        #
        # try:
        #     while window_size <= len(nums):
        #         for i in range(len(nums)):
        #             if i + window_size > len(nums):
        #                 break
        #             if i == 0:
        #                 window_sum = sum(nums[:i + window_size])
        #             else:
        #                 window_sum = window_sum - nums[i - 1] + nums[i + window_size-1]
        #
        #             if window_sum % k == 0:
        #                 logger.info(f'window size: {window_size}')
        #                 logger.info(f'window: {nums[i:i + window_size]}')
        #                 logger.info(f'window sum: {window_sum} k: {k}')
        #                 return True
        #         window_size += 1
        #
        # except Exception as e:
        #     logger.exception(f'exception: {e}')
        # logger.info(f'window size: {window_size}')
        # return False

        # the following solution has a time complexity of O(n)
        remainder_mapping, sum = {0: -1}, 0

        try:
            for i, num in enumerate(nums):
                sum += num
                remainder = sum % k
                logger.info(f'remainder: {remainder}')
                if remainder not in remainder_mapping:
                    remainder_mapping[remainder] = i
                else:
                    if i - remainder_mapping[remainder] > 1:
                        return True

            return False

        except Exception as e:
            logger.exception(f'exception: {e}')


if __name__ == '__main__':
    starting_time = time.time()
    s = Solution()
    logger.info(s.checkSubarraySum([23, 2, 4, 6, 7], 6))
    ending_time = time.time()
    logger.info(f'Execution time: {(ending_time - starting_time) * 1000:.2f} ms')
