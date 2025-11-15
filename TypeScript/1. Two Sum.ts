function twoSum(nums: number[], target: number): number[] {
  try {
    let firstPointer = 0;
    let secondPointer = nums.length - 1;
    const sortedWithIndex = nums
      .map((value, index) => [value, index])
      .sort((a, b) => a[0] - b[0]);

    while (
      sortedWithIndex[firstPointer][0] + sortedWithIndex[secondPointer][0] !==
      target
    ) {
      if (
        sortedWithIndex[firstPointer][0] + sortedWithIndex[secondPointer][0] >
        target
      ) {
        secondPointer -= 1;
      } else if (
        sortedWithIndex[firstPointer][0] + sortedWithIndex[secondPointer][0] <
        target
      ) {
        firstPointer += 1;
      }
    }

    return [
      sortedWithIndex[firstPointer][1],
      sortedWithIndex[secondPointer][1],
    ];
  } catch (error) {
    throw error;
  }
}

function main() {
  console.log(twoSum([2, 7, 11, 15], 9));
}

main();
