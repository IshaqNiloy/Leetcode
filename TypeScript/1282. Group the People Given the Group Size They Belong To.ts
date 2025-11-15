function groupThePeople(groupSizes: number[]): number[][] {
  try {
    const groups: number[][] = [];
    const groupSizeGroupMapping: Record<number, number[]> = {};

    for (let i = 0; i < groupSizes.length; i++) {
      if (groupSizes[i] in groupSizeGroupMapping) {
        groupSizeGroupMapping[groupSizes[i]].push(i);
      } else {
        groupSizeGroupMapping[groupSizes[i]] = [i];
      }

      if (groupSizeGroupMapping[groupSizes[i]].length === groupSizes[i]) {
        groups.push(groupSizeGroupMapping[groupSizes[i]]);
        groupSizeGroupMapping[groupSizes[i]] = [];
      }
    }
    return groups;
  } catch (error) {
    throw error;
  }
}

function main() {
  console.log(groupThePeople([2, 1, 3, 3, 3, 2]));
}

main();
