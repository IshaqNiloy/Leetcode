function largestPerimeter(nums: number[]): number {
  const sortedNums = nums.sort((a, b) => a - b);

  for (let i = sortedNums.length - 1; i >= 2; i--) {
    // The three sides will always be three consecutive numbers after sorting
    if (sortedNums[i - 1] + sortedNums[i - 2] > sortedNums[i]) {
      return sortedNums[i - 1] + sortedNums[i - 2] + sortedNums[i];
    }
  }
  return 0;
}

function main() {
  console.log(largestPerimeter([3, 6, 2, 3]));
}

main();
