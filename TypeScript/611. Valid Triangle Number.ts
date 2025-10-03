function triangleNumber(nums: number[]): number {
  let validTriangleNum = 0;
  const sortedNums = nums.sort((a, b) => a - b);

  for (let i = 0; i < sortedNums.length; i++) {
    for (let j = i + 1; j < sortedNums.length; j++) {
      for (let k = j + 1; k < sortedNums.length; k++) {
        if (sortedNums[i] + sortedNums[j] > sortedNums[k]) {
          validTriangleNum += 1;
        } else {
          break;
        }
      }
    }
  }
  return validTriangleNum;
}

function main() {
  console.log(triangleNumber([4, 2, 3, 4]));
}

main();
