function containsDuplicate(nums: number[]): boolean {
  try {
    const numberFrequencyMapping: Record<number, number> = {};

    for (const num of nums) {
      if (!(num in numberFrequencyMapping)) {
        numberFrequencyMapping[num] = 1;
      } else {
        return true;
      }
    }

    return false;
  } catch (error) {
    throw error;
  }
}

function main() {
  console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]));
}

main();
