class Solution {
  /**
   * @param {number[]} nums
   * @param {number} k
   * @return {number[]}
   */
  topKFrequent(nums: number[], k: number) {
    try {
      const numberFrequencyMapping: any = {};
      let result = [];

      for (const num of nums) {
        if (num in numberFrequencyMapping) {
          numberFrequencyMapping[num] += 1;
        } else {
          numberFrequencyMapping[num] = 1;
        }
      }

      result = Object.entries(numberFrequencyMapping).sort(
        (a: any, b: any) => b[1] - a[1]
      );

      return result.map((item) => Number(item[0])).slice(0, k);
    } catch (error) {
      console.log(error);
    }
  }
}

function main() {
  const obj = new Solution();
  console.log(obj.topKFrequent([1, 2, 2, 3, 3, 3], 2));
}

main();
