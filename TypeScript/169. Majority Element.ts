function majorityElement(nums: number[]): number {
  try {
    let max: number = 0,
      majorityElement: number = 0;
    const numberFrequencyMapping: Record<number, number> = {};

    for (const num of nums) {
      if (num in numberFrequencyMapping) {
        numberFrequencyMapping[num] += 1;
      } else {
        numberFrequencyMapping[num] = 1;
      }
    }
    for (const key in numberFrequencyMapping) {
      if (numberFrequencyMapping[key] > max) {
        majorityElement = Number(key);
        max = numberFrequencyMapping[key];
      }
    }

    return majorityElement;
  } catch (error) {
    throw error;
  }
}

function main() {
  console.log(majorityElement([3, 3, 4]));
}

main();
