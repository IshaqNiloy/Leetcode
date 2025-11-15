/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
  try {
    for (const num of nums2) {
      nums1[m] = num;
      m += 1;
    }
    nums1.sort((a, b) => a - b);
  } catch (error) {
    throw error;
  }
}

function main() {
  merge([0], 0, [1], 1);
}
main();
