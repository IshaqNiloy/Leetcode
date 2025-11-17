function kLengthApart(nums: number[], k: number): boolean {
  try {
    let firstPointer: number = 0;

    // Find the first index containing 1
    for (let i = 0; i < nums.length; i++) {
      if (nums[i] === 1) {
        firstPointer = i;
        break;
      }
    }

    // Find the second pointer
    let secondPointer: number = firstPointer + 1;

    // Calculate each difference between the firstPointer and secondPointer and check whether that difference is less than k. If it is less than k then it means it does not cover the difference. So return false.
    while (secondPointer < nums.length) {
      if (nums[secondPointer] === 1) {
        if (secondPointer - firstPointer - 1 < k) {
          return false;
        } else {
          firstPointer = secondPointer;
        }
      }
      secondPointer += 1;
    }

    return true;
  } catch (error) {
    throw error;
  }
}

function main() {
  console.log(kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2));
}

main();
