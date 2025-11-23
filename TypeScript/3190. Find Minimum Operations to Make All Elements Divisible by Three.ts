function minimumOperations(nums: number[]): number {
  try {
    let minimumNumsOfOps: number = 0;
    for (const num of nums) {
      let remainder: number = num % 3;
      if (remainder === 0) minimumNumsOfOps += 0;
      else if (remainder === 1 || remainder === 2) minimumNumsOfOps += 1;
    }

    return minimumNumsOfOps;
  } catch (error) {
    throw error;
  }
}

console.log(minimumOperations([3, 6, 9]));

// You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

// Return the minimum number of operations to make all elements of nums divisible by 3.
