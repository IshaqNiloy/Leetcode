function groupAnagrams(strs: string[]): string[][] {
  try {
    const wordGroupMapping: any = {};

    for (const str of strs) {
      const sortedStr = str.split("").sort().join("");
      if (sortedStr in wordGroupMapping) {
        wordGroupMapping[sortedStr].push(str);
      } else {
        wordGroupMapping[sortedStr] = [str];
      }
    }

    return Object.values(wordGroupMapping);
  } catch (error) {
    throw error;
  }
}

function main() {
  console.log(groupAnagrams(["a"]));
}

main();
