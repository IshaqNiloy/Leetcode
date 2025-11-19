function findFinalValue(nums: number[], original: number): number {
  try {
    const sortedNums: number[] = nums.sort((a, b) => a - b);

    for (let i = 0; i < sortedNums.length; i++) {
      if (sortedNums[i] === original) {
        original *= 2;
      }
    }
    return original;
  } catch (error) {
    throw error;
  }
}

console.log(findFinalValue([8, 19, 4, 2, 15, 3], 2));
