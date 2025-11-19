function threeSum(nums: number[]): number[][] {
  try {
    const result: any = [];

    const sortedNums = nums.sort((a: any, b: any) => a - b);

    for (let i = 0; i < sortedNums.length; i++) {
      // Skip duplicates
      if (i > 0 && sortedNums[i] === sortedNums[i - 1]) continue;

      let firstPointer = i + 1;
      let secondPointer = sortedNums.length - 1;

      while (firstPointer < secondPointer) {
        const sum =
          sortedNums[i] + sortedNums[firstPointer] + sortedNums[secondPointer];
        if (sum > 0) {
          secondPointer -= 1;
        } else if (sum < 0) {
          firstPointer += 1;
        } else if (sum === 0) {
          result.push([
            sortedNums[i],
            sortedNums[firstPointer],
            sortedNums[secondPointer],
          ]);

          // Looking forward to skip duplicates for firstPointer and secondPointer
          while (
            firstPointer < secondPointer &&
            sortedNums[firstPointer] === sortedNums[firstPointer + 1]
          ) {
            firstPointer += 1;
          }

          while (
            firstPointer < secondPointer &&
            sortedNums[secondPointer] === sortedNums[secondPointer - 1]
          ) {
            secondPointer -= 1;
          }

          firstPointer += 1;
          secondPointer -= 1;
        }
      }
    }
    return result;
  } catch (error) {
    throw error;
  }
}

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
